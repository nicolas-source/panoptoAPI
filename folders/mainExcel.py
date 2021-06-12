from uploader import startUploadExcel
from downloader import obtainLinksFromFolder
from reader import parse_argument


def main():
    args = parse_argument()
    startUploadExcel(args.location, args.sheetName, args.row, args.col)
    obtainLinksFromFolder()

if __name__ == '__main__':
    main()