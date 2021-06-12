from uploader import *
from downloader import obtainLinksFromFolder
from reader import *


def main():
    folderID = input("Folder ID: ")
    args = parse_argument()
    list = fromFileToList(args)
    startUpload(list, folderID)
    obtainLinksFromFolder(folderID)


def mainTest():
    args = parse_argument()
    print("---args---\n", args)
    list = fromFileToList(args)
    print("---list---\n", list)
    startUploadFullCredentials(list, args.folderID, args.username, args.password)
    obtainLinksFromFolder(args.folderID)


if __name__ == '__main__':
    mainTest()
    # main()
