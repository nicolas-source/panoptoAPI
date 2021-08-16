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


print("Original\n", parent_course_folder_df)

# print(parent_course_folder_df.duplicated(subset=["CourseName"]))

# print("Total non-func relations\n", parent_course_folder_df[parent_course_folder_df.duplicated(subset=["CourseName"])])
print("Total unique non-func relations\n", parent_course_folder_df[parent_course_folder_df.duplicated(subset=["CourseName"])].drop_duplicates(subset=["CourseName"]))
print("Total unique non-func relations length\n", len(parent_course_folder_df[parent_course_folder_df.duplicated(subset=["CourseName"])].drop_duplicates(subset=["CourseName"])))






