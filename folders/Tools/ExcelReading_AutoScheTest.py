import pandas as pd

currentSheet_DataFrame = pd.read_excel(
    open("Automated Scheduling Test Local.xlsx", 'rb'),
    sheet_name='Panopto Folders to Create')

parent_course_folder_df = currentSheet_DataFrame[['Division Folder', 'Course Level Folder']]

parent_course_folder_df = parent_course_folder_df.dropna()
parent_course_folder_df.columns = ['ParentName', 'CourseName']
parent_course_folder_df = parent_course_folder_df.drop_duplicates()

data = []
prev = None

print("Original\n", parent_course_folder_df)

# print(parent_course_folder_df.duplicated(subset=["CourseName"]))

# print("Total non-func relations\n", parent_course_folder_df[parent_course_folder_df.duplicated(subset=["CourseName"])])

uniqueNonFuncRelations = parent_course_folder_df[
    parent_course_folder_df.duplicated(subset=["CourseName"])].drop_duplicates(subset=["CourseName"])
print("Total unique non-func relations\n",
      parent_course_folder_df[parent_course_folder_df.duplicated(subset=["CourseName"])].drop_duplicates(
          subset=["CourseName"]))
print("Total unique non-func relations length\n", len(
    parent_course_folder_df[parent_course_folder_df.duplicated(subset=["CourseName"])].drop_duplicates(
        subset=["CourseName"])))

print(uniqueNonFuncRelations["CourseName"])
print(len(uniqueNonFuncRelations["CourseName"]))

print(parent_course_folder_df["CourseName"].isin(uniqueNonFuncRelations["CourseName"]))
print(parent_course_folder_df[~parent_course_folder_df["CourseName"].isin(uniqueNonFuncRelations["CourseName"])])
filtered_parent_course_folder_df = parent_course_folder_df[
    ~parent_course_folder_df["CourseName"].isin(uniqueNonFuncRelations["CourseName"])]

for index, row in uniqueNonFuncRelations.iterrows():
    row["ParentName"] = "Program Wide Courses"

print(uniqueNonFuncRelations)

completeMapping = filtered_parent_course_folder_df.append(uniqueNonFuncRelations, ignore_index=True)
print(completeMapping)
completeMapping.to_csv("CompletedList.csv")

from tabulate import tabulate

print(tabulate(completeMapping, headers='keys', tablefmt='psql'))
