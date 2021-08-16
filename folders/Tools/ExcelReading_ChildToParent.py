import pandas as pd
from difflib import SequenceMatcher
from tabulate import tabulate

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
        current_rating = SequenceMatcher(None, childOrigin_df["Name"][originInd], parentDest_df['ChildChildName'][destInd]).ratio()
        if current_rating > best_rating:
            best_rating = current_rating
            best_rating_index = destInd
    print(best_rating, best_rating_index)
    matchingList.append((childOrigin_df["Name"][originInd], parentDest_df['ChildChildName'][best_rating_index]))
        # print(childOrigin_df["Name"][originInd])
        # print(parentDest_df['ChildChildName'][destInd])



print(matchingList)

print(tabulate(matchingList))
print("Length\n", len(matchingList))