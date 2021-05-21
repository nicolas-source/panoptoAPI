import csv

# with open('inputCSV.csv', mode='r', encoding='utf-8-sig') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             # print(dict(row))
#             line_count += 1
#         # print(f'\t{row["StudentNumber"]} works in the {row["StudentName"]} department, and was born in {row["Notes"]}.')
#         # print(dict(row))
#         print(f'{row["StudentNumber"]}_{row["StudentName"]}')
#         line_count += 1
#     print(f'Processed {line_count} lines.')



def csvListOfDicts():
    with open('csvFiles/inputCSV.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list = []
        for row in csv_reader:
            list.append(row)

        return list

# print(csvListOfDicts())