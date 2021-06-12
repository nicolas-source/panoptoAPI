import csv
from openpyxl import load_workbook
import argparse


# Input: CSV Column
# Output: CSV Column as list
def csvListOfDicts():
    with open('csvFiles/inputCSV.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list = []
        for row in csv_reader:
            list.append(row)

        return list


# Input: ExcelFile, ExcelSheet, ExcelColumn
# Output: ExcelColumn as list of dicts
def excelListOfDicts(excelFileName, excelSheetName, excelRow, excelCol):
    excelWorkbook = load_workbook(excelFileName)
    list = []

    while excelWorkbook[excelSheetName][excelCol + str(excelRow)].value is not None:
        list.append(excelWorkbook[excelSheetName][excelCol + str(excelRow)].value)
        excelRow += 1

    return list


def parse_argument():
    parser = argparse.ArgumentParser(description='Argument Parser')
    parser.add_argument("--folderID", required=False, dest="folderID", help="Panopto destination folder ID")
    parser.add_argument('--fileLocation', dest="location", help='Excel File Location')
    parser.add_argument("--sheet", dest="sheetName", help='Excel Sheet Name')
    parser.add_argument("--column", dest="col",help='Excel Column')
    parser.add_argument("--row", dest="row", help='Excel Row')
    return parser.parse_args()



args = parse_argument()



print(args.folderID)
print(args.location)
print(args.sheetName)
print(args.col)
print(args.row)

#
# excelFileName = "excelFiles/inputCSV.xlsx"
# excelSheetName = "inputCSV"
# excelRow = 2
# excelCol = "B"
#
# excelListOfDicts(excelFileName, excelSheetName, excelRow, excelCol)

