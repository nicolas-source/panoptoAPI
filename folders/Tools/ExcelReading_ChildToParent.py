import pandas as pd
from difflib import SequenceMatcher
from tabulate import tabulate
import csv

parentDest_df = pd.read_csv(
    open("../csvFiles/outputParentDest.csv", 'rb'))

childOrigin_df = pd.read_csv(
    open("../csvFiles/outputChildOrigin.csv", 'rb'))

# print(parentDest_df['ChildChildName'])
# print(childOrigin_df['Name'])

# for origin in childOrigin_df['Name'].iteritems():
#     print(origin[1])
# for dest in parentDest_df['ChildChildName'].iteritems():
#     print(origin)
#     print(dest)

# parentDest_df = parentDest_df.head(100)
# childOrigin_df = childOrigin_df.head(100)

matchingList = []

for originInd in childOrigin_df.index:
    best_rating = 0;
    best_rating_index = 0;
    for destInd in parentDest_df.index:
        current_rating = SequenceMatcher(None, childOrigin_df["Name"][originInd],
                                         parentDest_df['ChildChildName'][destInd]).ratio()
        if current_rating > best_rating:
            best_rating = current_rating
            best_rating_index = destInd
    print(best_rating, best_rating_index)
    matchingList.append((originInd, childOrigin_df["Name"][originInd], best_rating_index,
                         parentDest_df['ChildChildName'][best_rating_index]))
    # print(childOrigin_df["Name"][originInd])
    # print(parentDest_df['ChildChildName'][destInd])

print(matchingList)

print(tabulate(matchingList))
print("Length\n", len(matchingList))

# matchingList.pop(143) v
# matchingList.pop(142) v
# matchingList.pop(135) v
# matchingList.pop(134) v
# matchingList.pop(133) v
# matchingList.pop(132) v
# matchingList.pop(131) v
# matchingList.pop(130) v
# matchingList.pop(72) (391->439)
# matchingList.pop(71) (391->439)
# matchingList.pop(60) v
# matchingList.pop(59) v
matchingList.pop(0)

print(tabulate(matchingList))
print("Length\n", len(matchingList))

pieced_list = []
#
# print(childOrigin_df['ChildName'])
# print(childOrigin_df['ChildId'].iloc[4])
print(parentDest_df['ChildChildName'][155])
print(parentDest_df['ChildChildId'][155])

for theTuple in matchingList:
    a = theTuple[0]
    b = theTuple[1]
    c = theTuple[2]
    d = theTuple[3]

    # pieced_list.append([childOrigin_df['ChildName'].iloc[a], childOrigin_df[a]['ChildId'].iloc[a], parentDest_df['ChildChildName'].iloc[c], parentDest_df[c]['ChildChildId'].iloc[c]])
    print(childOrigin_df['ChildName'].iloc[a])
    print(childOrigin_df['ChildId'].iloc[a])
    print(parentDest_df['ChildChildName'].iloc[c])
    print(parentDest_df['ChildChildId'].iloc[c])

    pieced_list.append({'Index': a,
                        'ParentName': childOrigin_df['Name'].iloc[a],
                        'ParentId': childOrigin_df['Id'].iloc[a],
                        'ChildName': childOrigin_df['ChildName'].iloc[a],
                        'ChildId': childOrigin_df['ChildId'].iloc[a],
                        'NewParentName': parentDest_df['ChildChildName'].iloc[c],
                        'NewParentId': parentDest_df['ChildChildId'].iloc[c]
                        })

print(tabulate(pieced_list))

keys = pieced_list[0].keys()
with open('../csvFiles/piecedList.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(pieced_list)
