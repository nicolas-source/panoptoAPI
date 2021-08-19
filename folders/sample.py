#!python3
import sys
import argparse
import requests
import urllib3
import csv
import os.path
import time
from os import path

from credentials import *

from panopto_folders import PanoptoFolders

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..', 'common')))
from panopto_oauth2 import PanoptoOAuth2

# Top level folder is represented by zero GUID.
# However, it is not the real folder and some API beahves differently than actual folder.
GUID_TOPLEVEL = '00000000-0000-0000-0000-000000000000'


def parse_argument():
    parser = argparse.ArgumentParser(description='Sample of Folders API')
    parser.add_argument('--server', dest='server', required=True, help='Server name as FQDN')
    parser.add_argument('--client-id', dest='client_id', required=True, help='Client ID of OAuth2 client')
    parser.add_argument('--client-secret', dest='client_secret', required=True, help='Client Secret of OAuth2 client')
    parser.add_argument('--skip-verify', dest='skip_verify', action='store_true', required=False,
                        help='Skip SSL certificate verification. (Never apply to the production code)')
    return parser.parse_args()


class modifiedArg():
    def __init__(self, server, client_id, client_secret):
        self.server = server
        self.client_id = client_id
        self.client_secret = client_secret
        self.skip_verify = True


def main():
    # args = parse_argument()   # Edited
    args = modifiedArg(server,
                       clientID,
                       clientSecret)

    if args.skip_verify:
        # This line is needed to suppress annoying warning message.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Use requests module's Session object in this example.
    # ref. https://2.python-requests.org/en/master/user/advanced/#session-objects
    requests_session = requests.Session()
    requests_session.verify = not args.skip_verify

    # Load OAuth2 logic
    oauth2 = PanoptoOAuth2(args.server, args.client_id, args.client_secret, not args.skip_verify)

    # Load Folders API logic
    folders = PanoptoFolders(args.server, not args.skip_verify, oauth2)

    current_folder_id = GUID_TOPLEVEL

    while True:
        print('----------------------------')
        current_folder = get_and_display_folder(folders, current_folder_id)
        sub_folders = get_and_display_sub_folders(folders, current_folder_id)
        current_folder_id = process_selection(folders, current_folder, sub_folders)


def get_and_display_folder(folders, folder_id):
    '''
    Returning folder object that is returned by API.
    None if it is top level folder.
    '''
    print()
    print('Folder:')
    if folder_id == GUID_TOPLEVEL:
        print('  Top level folder (no detail informaiton is available)')
        return None

    folder = folders.get_folder(folder_id)
    print('  Name: {0}'.format(folder['Name']))
    print('  Id: {0}'.format(folder['Id']))
    if folder['ParentFolder'] is None:
        print('  Parent Folder: Top level folder')
    else:
        print('  Parent Folder: {0}'.format(folder['ParentFolder']['Name']))
    print('  Folder URL: {0}'.format(folder['Urls']['FolderUrl']))
    print('  Embed URL: {0}'.format(folder['Urls']['EmbedUrl']))
    print('  Share settings URL: {0}'.format(folder['Urls']['ShareSettingsUrl']))
    return folder


def get_and_display_sub_folders(folders, current_folder_id):
    print()
    print('Sub Folders:')
    children = folders.get_children(current_folder_id)

    # returning object is the dictionary, key (integer) and folder's ID (UUID)
    result = {}
    key = 0
    for entry in children:
        result[key] = entry['Id']
        print('  [{0}]: {1}'.format(key, entry['Name']))
        key += 1

    return result


def get_and_print_sub_folders_3Levels(folders, current_folder_id):
    with open("csvFiles/outputParent.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Name', 'Id', 'ChildName', 'ChildId'])

        print()
        print('Sub Folders:')
        children = folders.get_children(current_folder_id)
        # returning object is the dictionary, key (integer) and folder's ID (UUID)
        result = {}
        key = 0

        # for entry in children:
        #     result[key] = entry['Id']
        #     print('  [{0}]: {1} : {2}'.format(key, entry['Name'], entry['Id']))
        #     writer.writerow([entry['Name'], entry['Id']])
        #     key += 1

        for entry in children:
            result[key] = entry['Id']
            # print('  [{0}]: {1} : {2}'.format(key, entry['Name'], entry['Id']))
            # writer.writerow([entry['Name'], entry['Id']])
            key += 1

            childrenchildren = folders.get_children(entry['Id'])
            for entryentry in childrenchildren:
                time.sleep(5)
                result[key] = entryentry['Id']
                # print('  [{0}]: {1} : {2}'.format(key, entry['Name'], entry['Id']))
                # writer.writerow([entry['Name'], entry['Id'], entryentry['Name'], entryentry['Id']])
                key += 1

                childrenchildrenchildren = folders.get_children(entryentry['Id'])
                for entryentryentry in childrenchildrenchildren:
                    result[key] = entryentryentry['Id']
                    # print('  [{0}]: {1} : {2}'.format(key, entry['Name'], entry['Id']))
                    writer.writerow(
                        [entry['Name'], entry['Id'], entryentry['Name'], entryentry['Id'], entryentryentry['Name'],
                         entryentryentry['Id']])
                    key += 1

    return result


def get_and_print_sub_folders_2Levels(folders, current_folder_id):
    with open("csvFiles/outputParent.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Name', 'Id', 'ChildName', 'ChildId'])

        print()
        print('Sub Folders:')
        children = folders.get_children(current_folder_id)
        # returning object is the dictionary, key (integer) and folder's ID (UUID)
        result = {}
        key = 0

        # for entry in children:
        #     result[key] = entry['Id']
        #     print('  [{0}]: {1} : {2}'.format(key, entry['Name'], entry['Id']))
        #     writer.writerow([entry['Name'], entry['Id']])
        #     key += 1

        for entry in children:
            result[key] = entry['Id']
            # print('  [{0}]: {1} : {2}'.format(key, entry['Name'], entry['Id']))
            # writer.writerow([entry['Name'], entry['Id']])
            key += 1
            time.sleep(10)
            childrenchildren = folders.get_children(entry['Id'])
            for entryentry in childrenchildren:
                time.sleep(1)
                result[key] = entryentry['Id']
                # print('  [{0}]: {1} : {2}'.format(key, entry['Name'], entry['Id']))
                writer.writerow([entry['Name'], entry['Id'], entryentry['Name'], entryentry['Id']])
                key += 1

    return result


def listFoldersToCSV(folders, current_folder_id):
    original = "outputFoldersCSV"
    name = "outputFoldersCSV"

    print("Checking file existance")

    # global counter
    counter = 0
    while path.exists('csvFiles/' + name + ".csv"):
        counter = counter + 1
        name = name + str(counter)

    print('Writing to CSV:')

    with open('csvFiles/' + original + str(counter) + ".csv", mode='w') as csv_file:

        fieldnames = ['Name', 'Id', 'Parent Name', 'Parent Id']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for entry in folders.get_children(current_folder_id):
            writer.writerow({'Name': entry['Name'],
                             'Id': entry['Id'],
                             'Parent Name': entry['ParentFolder']['Name'],
                             'Parent Id': entry['ParentFolder']['Id']
                             })


def process_selection(folders, current_folder, sub_folders):
    if current_folder is None:
        new_folder_id = GUID_TOPLEVEL
        parent_folder_id = GUID_TOPLEVEL
    else:
        new_folder_id = current_folder['Id']
        if current_folder['ParentFolder'] is None:
            parent_folder_id = GUID_TOPLEVEL
        else:
            parent_folder_id = current_folder['ParentFolder']['Id']

    print()
    print('[P] Go to parent')
    print('[R] Rename this parent folder ID')
    print('[D] Delete this folder')
    print('[S] Search folders')
    print('[L] List sessions in the folder')
    print('[C] List folders to CSV')
    print('[A] List folders to from folder Id')
    print()
    selection = input('Enter the command (select number to move folder): ')

    try:
        key = int(selection)
        if sub_folders[key]:
            return sub_folders[key]
    except:
        pass  # selection is not a number, fall through

    if selection.lower() == 'p':
        new_folder_id = parent_folder_id
    elif selection.lower() == 'r' and current_folder is not None:
        # rename_folder(folders, current_folder)
        redef_parent_folder(folders, current_folder)  # Edited
    elif selection.lower() == 'd' and current_folder is not None:
        if delete_folder(folders, current_folder):
            new_folder_id = parent_folder_id
    elif selection.lower() == 's':
        result = search_folder(folders)
        if result is not None:
            new_folder_id = result
    elif selection.lower() == 'l' and current_folder is not None:
        list_sessions(folders, current_folder)
    elif selection.lower() == 'c' and current_folder is not None:
        listFoldersToCSV(folders, parent_folder_id)
    elif selection.lower() == 'a' and current_folder is not None:
        folder_id = input("Enter folder Id: ")
        get_and_print_sub_folders_3Levels(folders, folder_id)
    else:
        print('Invalid command.')

    return new_folder_id


def rename_folder(folders, folder):
    new_name = input('Enter new name: ')
    return folders.update_folder_name(folder['Id'], new_name)


def redef_parent_folder(folders, targetFolder, newParentFolder):
    # new_name = input('Enter new name: ')
    return folders.update_folder_json(targetFolder['Id'], newParentFolder)


def redef_parent_folder_DirectID(folders, targetFolder, newParentFolder):
    # new_name = input('Enter new name: ')
    return folders.update_folder_json(targetFolder, newParentFolder)


def delete_folder(folders, folder):
    return folders.delete_folder(folder['Id'])


def search_folder(folders):
    query = input('Enter search keyword: ')
    entries = folders.search_folders(query)

    if len(entries) == 0:
        print('  No hit.')
        return None

    for index in range(len(entries)):
        print('  [{0}]: {1}'.format(index, entries[index]['Name']))
    selection = input('Enter the number (or just enter to stay current): ')

    new_folder_id = None
    try:
        index = int(selection)
        if 0 <= index < len(entries):
            new_folder_id = entries[index]['Id']
    except:
        pass

    return new_folder_id


def mainGetSubFolders():
    args = modifiedArg(server,
                       clientID,
                       clientSecret)

    if args.skip_verify:
        # This line is needed to suppress annoying warning message.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Use requests module's Session object in this example.
    # ref. https://2.python-requests.org/en/master/user/advanced/#session-objects
    requests_session = requests.Session()
    requests_session.verify = not args.skip_verify

    # Load OAuth2 logic
    oauth2 = PanoptoOAuth2(args.server, args.client_id, args.client_secret, not args.skip_verify)

    # Load Folders API logic
    folders = PanoptoFolders(args.server, not args.skip_verify, oauth2)

    # folder_id = input("Enter folder Id: ")
    # folder_id = "8e2870f9-ea9c-468a-9d13-aaf6017f2f06"
    folder_id = "5c732159-f30c-45a1-a29e-8560bdf73528"
    get_and_print_sub_folders_2Levels(folders, folder_id)


def mainRefDefParentFolders():
    args = modifiedArg(server,
                       clientID,
                       clientSecret)

    if args.skip_verify:
        # This line is needed to suppress annoying warning message.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Use requests module's Session object in this example.
    # ref. https://2.python-requests.org/en/master/user/advanced/#session-objects
    requests_session = requests.Session()
    requests_session.verify = not args.skip_verify

    # Load OAuth2 logic
    oauth2 = PanoptoOAuth2(args.server, args.client_id, args.client_secret, not args.skip_verify)

    # Load Folders API logic
    folders = PanoptoFolders(args.server, not args.skip_verify, oauth2)

    # Start of re def parent Id logic

    # Test with single re def
    targetFolder_id = "ab7f393a-b465-4945-9d42-ad8701215e84"
    newParentFolder_id = "e6e4905f-d2eb-4a67-aee5-acb1003f3086"
    redef_parent_folder_DirectID(folders, targetFolder_id, newParentFolder_id)
    # get_and_display_sub_folders(folders, newParentFolder_id)

    # Test with 2 re defs
    Folder1 = "e6e4905f-d2eb-4a67-aee5-acb1003f3086"
    Folder2 = "800f6ab8-3cb0-4c85-aac1-acb100427930"

    SubFolder1 = "137b4a76-9642-4824-b4a9-ad870124e6d2"
    SubFolder2 = "ab7f393a-b465-4945-9d42-ad8701215e84"

    combinedList = []
    # combinedList.append({"Child": SubFolder1, "Parent": Folder1})
    # combinedList.append({"Child": SubFolder2, "Parent": Folder2})
    print(combinedList)

    with open('csvFiles/piecedList.csv') as csvfile:
        # read the file
        reader = csv.DictReader(csvfile)

        # for every line in the csv
        for row in reader:
            # create a friend tuple
            combinedList.append(row)
    import tabulate


    for entry in combinedList:
        print((entry["ChildName"], entry["NewParentName"]))

    log = []

    # for entry in combinedList:
    #     time.sleep(2)
    #     redef_parent_folder_DirectID(folders, entry["ChildId"], entry["NewParentId"])
    #     log.append({"ChildId": entry["ChildId"], "NewParentId": entry["NewParentId"]})

    keys = log[0].keys()
    with open('csvFiles/ParentFolderReassignOperationsLog.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(log)

def mainRefDefParentFoldersManual():
    args = modifiedArg(server,
                       clientID,
                       clientSecret)

    if args.skip_verify:
        # This line is needed to suppress annoying warning message.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Use requests module's Session object in this example.
    # ref. https://2.python-requests.org/en/master/user/advanced/#session-objects
    requests_session = requests.Session()
    requests_session.verify = not args.skip_verify

    # Load OAuth2 logic
    oauth2 = PanoptoOAuth2(args.server, args.client_id, args.client_secret, not args.skip_verify)

    # Load Folders API logic
    folders = PanoptoFolders(args.server, not args.skip_verify, oauth2)

    # Start of re def parent Id logic

    # Test with single re def
    targetFolder_id = "ab7f393a-b465-4945-9d42-ad8701215e84"
    newParentFolder_id = "e6e4905f-d2eb-4a67-aee5-acb1003f3086"
    redef_parent_folder_DirectID(folders, targetFolder_id, newParentFolder_id)
    # get_and_display_sub_folders(folders, newParentFolder_id)

    # Test with 2 re defs

    COMM486F = "3b7754cb-fbe8-43af-9591-ad87016ec8e2"
    COMM486M = "24790c1f-b380-4033-8b4e-ad87016f1763"
    COMM486U = "fe3294b5-8df9-4c93-b838-ad87016f4e10"

    COMM386U = "fe3294b5-8df9-4c93-b838-ad87016f4e10"
    Old_COMM391 = "c1a0d63c-9505-4a23-8895-fa5d3d4c656c"


    combinedList = []
    # combinedList.append({"ChildId": "76e81964-0c8e-4701-b1ff-6bf5a61a279b", "NewParentId": COMM486F})
    # combinedList.append({"ChildId": "fa526c6f-b322-4d3f-a016-e16f94acf108", "NewParentId": COMM486M})
    # combinedList.append({"ChildId": "3b057d07-54f3-4afd-b8d0-9a539f0b9536", "NewParentId": COMM486M})
    # combinedList.append({"ChildId": "f7000f07-3721-4831-b858-ab7c016a9aa1", "NewParentId": COMM486M})
    # combinedList.append({"ChildId": "76c728ad-f3ec-4e75-8e6d-cba7400a8871", "NewParentId": COMM486U})
    # combinedList.append({"ChildId": "e0a43c7a-b261-467e-bb9e-b08a97d883c8", "NewParentId": COMM486U})

    combinedList.append({"ChildId": "1d45eb6d-1392-4b45-98e8-ad1b502890e3", "NewParentId": Old_COMM391})
    combinedList.append({"ChildId": "08e69f41-f058-4740-a0fd-8c5862b85c9e", "NewParentId": Old_COMM391})

    print(combinedList)


    log = []

    for entry in combinedList:
        time.sleep(1)
        # redef_parent_folder_DirectID(folders, entry["ChildId"], entry["NewParentId"])
        log.append({"ChildId": entry["ChildId"], "NewParentId": entry["NewParentId"]})

    keys = log[0].keys()
    with open('logManual.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(log)


def list_sessions(folders, folder):
    print('Sessions in the folder:')
    for entry in folders.get_sessions(folder['Id']):
        print('  {0}: {1}'.format(entry['Id'], entry['Name']))


if __name__ == '__main__':
    # main()
    # mainGetSubFolders()
    # mainRefDefParentFolders()
    mainRefDefParentFoldersManual()