from zeep import Client
from reader import csvListOfDicts
from reader import excelListOfDicts
# from credentials import *
import getpass
import time

# folder = None
username = None
password = None


# Deprecated
def create_panopto_session():
    x = input("Session name:")

    site_name = 'sauderlearningservices.hosted.panopto.com'
    client = Client('https://{}/Panopto/PublicAPI/4.6/SessionManagement.svc?wsdl'.format(site_name))
    auth_info = {'Password': password, 'UserKey': username}

    panopto_session = client.service.AddSession(
        auth=auth_info,
        name=x,
        folderId=folder,
        isBroadcast=False
    )


# Creates an empty session on the Panopto server with the specified name
def create_panopto_session_name(name, folder):
    x = name

    site_name = 'sauderlearningservices.hosted.panopto.com'
    client = Client('https://{}/Panopto/PublicAPI/4.6/SessionManagement.svc?wsdl'.format(site_name))
    auth_info = {'Password': password, 'UserKey': username}

    panopto_session = client.service.AddSession(
        auth=auth_info,
        name=x,
        folderId=folder,
        isBroadcast=False
    )


def create_panopto_session_full_credentials(name, folderID, username, password):
    site_name = 'sauderlearningservices.hosted.panopto.com'
    client = Client('https://{}/Panopto/PublicAPI/4.6/SessionManagement.svc?wsdl'.format(site_name))
    auth_info = {'Password': password, 'UserKey': username}
    print("---Passing to panopto API---\n", name, folderID, username, password)
    panopto_session = client.service.AddSession(
        auth=auth_info,
        name=name,
        folderId=folderID,
        isBroadcast=False
    )


def getCredentials():
    # global folder
    global username
    global password
    # folder = input("Folder ID:")
    username = input("User:")
    password = getpass.getpass("Pass:")


def startUpload(list, folderID):
    getCredentials()

    if len(list) < 10:
        for entryName in list:
            print(entryName)
            create_panopto_session_name(entryName, folderID)
            time.sleep(.5)


def startUploadFullCredentials(list, folderID, username, password):
    if len(list) < 10:
        for entryName in list:
            print("entryName: ", entryName)
            create_panopto_session_full_credentials(entryName, folderID, username, password)
            time.sleep(.5)


# Deprecated
def startUploadCSV():
    if csvListOfDicts().__len__() < 10:
        for entry in csvListOfDicts():
            # print(entry)
            print(f'{entry["StudentName"]}_{entry["StudentNumber"]}')
            create_panopto_session_name(f'{entry["StudentName"]}_{entry["StudentNumber"]}')


# Deprecated
def startUploadExcel(excelFileName, excelSheetName, excelRow, excelCol):
    if excelListOfDicts(excelFileName, excelSheetName, excelRow, excelCol).__len__() < 10:
        for entry in excelListOfDicts(excelFileName, excelSheetName, excelRow, excelCol):
            # print(entry)
            # print(f'{entry["StudentName"]}_{entry["StudentNumber"]}')
            create_panopto_session_name(str(entry))

# ----Original Code----
# n = input("Num sessions?\n")
# n = int(n)
# if n < 10:
#     while n > 0:
#         create_panopto_session()
#         time.sleep(.5)
#         n = n-1
#         print("Done!")
# else:
#     print("While not started")
