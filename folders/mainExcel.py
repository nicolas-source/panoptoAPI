from uploader import startUploadExcel
from downloader import obtainLinks
from reader import parse_argument


def main():
    args = parse_argument()
    startUploadExcel(args.location, args.sheetName, args.row, args.col)
    obtainLinks()

if __name__ == '__main__':
    main()