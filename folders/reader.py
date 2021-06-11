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
def excelListOfDicts(excelFileName, excelSheetName, excelColumnName):
    excelWorkbook = load_workbook(excelFileName)

    list = []




def parse_argument():
    parser = argparse.ArgumentParser(description='Argument Parser')
    parser.add_argument('--folderID', help='Panopto upload destination folder ID')
    parser.add_argument("--sheet", help='Excel Sheet Name')
    parser.add_argument("--column", help='Excel Column Name')
    return parser.parse_args()
