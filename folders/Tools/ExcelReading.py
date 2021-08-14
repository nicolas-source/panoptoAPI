import pandas as pd

currentSheet_DataFrame = pd.read_excel(
    open("Automated Scheduling Test Local.xlsx", 'rb'),
    sheet_name='Panopto Folders to Create')

parent_course_folder_df = currentSheet_DataFrame[['Division Folder', 'Course Level Folder']]

parent_course_folder_df = parent_course_folder_df.dropna()
parent_course_folder_df.columns = ['ParentName', 'CourseName']

data = []
prev = None

multipleSharedCourses = [
    "COMM 101",
    "COMM 120",
    "COMM 186",
    "COMM 220",
    "COMM 292",
    "COMM 335",
    "COMM 386",
    "COMM 390",
    "COMM 394",
    "COMM 395"
]
multipleSharedCourses_df = pd.DataFrame(multipleSharedCourses, columns=["CourseName"])

# parent_course_folder_df.isin(multipleSharedCourses_df)

# parent_course_folder_df = parent_course_folder_df[
#     ~parent_course_folder_df['CourseName'].isin(multipleSharedCourses_df['CourseName'])]
#
# print(parent_course_folder_df)

funcData = []
nonFuncData = []

print("Original\n", parent_course_folder_df)

for index, row in parent_course_folder_df.iterrows():
    if row["CourseName"] in funcData:
        if row["CourseName"] in nonFuncData:
            continue
        else:
            nonFuncData.append({'ParentName': row["ParentName"], 'CourseName': row["CourseName"]})
    else:
        funcData.append({'ParentName': row["ParentName"], 'CourseName': row["CourseName"]})



funcData_df = pd.DataFrame(funcData)
nonFuncData_df = pd.DataFrame(nonFuncData)

print(funcData_df)
print(nonFuncData_df)


# for index, row in parent_course_folder_df.iterrows():
#     if prev != row["CourseName"]:
#         data.append({'ParentName': row["ParentName"], 'CourseName': row["CourseName"]})
#
#     prev = row["CourseName"]
#
#     # print(row["Division Folder"], row["Course Level Folder"])
#
# data_df = pd.DataFrame(data)

# print(multipleSharedCourses_df)
# print(data_df)
