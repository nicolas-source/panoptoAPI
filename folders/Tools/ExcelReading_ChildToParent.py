import pandas as pd

parentDest_df = pd.read_csv(
    open("../csvFiles/outputParentDest.csv", 'rb'))

print(parentDest_df)

childOrigin_df = pd.read_csv(
    open("../csvFiles/outputChildOrigin.csv", 'rb'))

print(childOrigin_df)