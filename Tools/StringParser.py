import pyparsing as pp
import csv

parseFormat = pp.Word(pp.alphas) + pp.Word(pp.alphanums) + \
         '-' + pp.Word(pp.alphas) + pp.Word(pp.alphanums) + pp.Word(pp.nums) + \
         '-' + pp.Word(pp.alphanums) + pp.Word(pp.alphas) + pp.Word(pp.printables) + pp.Word(pp.printables)

str1 = "LASR 102 - ARTH 322 001 - 2021W2 on 4/7/2022 (Thu)"
str2 = "BUCH B313 - GRSJ 224B 002 - 2021W2 on 4/7/2022 (Thu)"
#
# print(parseFormat.parseString(str1))
# print(parseFormat.parseString(str2))

sessionsList = []

with open('../folders/csvFiles/exportList.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sessionsList.append(row)


for x in sessionsList:
    print(x)

exportList = []

for session in sessionsList:
    try:
        parsed = parseFormat.parseString(session['Name'])
        exportList.append({'Name': session['Name'],
                           'Room': parsed[0] + " " + parsed[1],
                           'Course': parsed[3] + " " + parsed[4] + " " + parsed[5],
                           'Term': parsed[7],
                           'Date': parsed[9] + parsed[10],
                           'ViewerUrl': session['ViewerUrl'],
                           'Id': session['Id'],
                           'Folder Id': session['Folder Id']})
    except:
        print("Didn't parse this: " + session['Name'])

for x in exportList:
    print(x)

keys = exportList[0].keys()
with open('../folders/csvFiles/sessionsList.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(exportList)