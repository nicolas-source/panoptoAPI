import csv
from difflib import SequenceMatcher

list1 = []

with open('csvFiles/outputFoldersCSV.csv', newline='', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        list1.append({'Name': row['Name'], 'Id': row['Id'], 'Parent Name': row['Parent Name'], 'Parent Id': row['Parent Id']})

lista = list1[:31]
listb = list1[31:]


print("-----")
print(len(list1))
print("-----")
print(len(lista))
print("-----")
print(len(listb))




with open('csvFiles/outputOrganizedFoldersCSV.csv', mode='w') as csv_file:

    fieldnames = ['Name', 'Id', 'Parent Name', 'Parent Id', 'Sequence Ratio']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for a in lista:
        for b in listb:
            s = SequenceMatcher(None, a['Name'], b['Name'])
            print(s.ratio())
            writer.writerow({'Name': a['Name'],
                             'Id': a['Id'],
                             'Parent Name': b['Parent Name'],
                             'Parent Id': b['Parent Id'],
                             'Sequence Ratio': s.ratio()
                             })