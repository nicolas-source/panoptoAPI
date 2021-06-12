from zeep import Client

# from Users.nicolas.Library.Python.3.8.lib.python.site-packages.zeep import Client

from reader import csvListOfDicts
from reader import excelListOfDicts
from credentials import *

# folder = input("Folder ID:")
# u_name = input("User:")
# p_word = getpass.getpass("Pass:")





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
def create_panopto_session_name(name):
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


def startUploadCSV():
    if csvListOfDicts().__len__() < 10:
        for entry in csvListOfDicts():
            # print(entry)
            print(f'{entry["StudentName"]}_{entry["StudentNumber"]}')
            create_panopto_session_name(f'{entry["StudentName"]}_{entry["StudentNumber"]}')


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