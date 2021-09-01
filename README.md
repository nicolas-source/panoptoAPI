# Panopto API Scripts

1. Scraping scheduled recorded sessions' Ids and returning sessions info (e.g. viewerlinks)
2. Organizing Folders
3. Creating and uploading empty sessions

----------------------------------------
### Panopto API with Python (Scraping scheduled recorded sessions)

Run panoptoAPI/selenium/scraper.py 
Enter Username & Password
Returns csv of scheduled recorded sessions' info
Can set number of scheduled recorded sessions desired based on how many are listed at once in the browser page
  -> Currently hard-coded


----------------------------------------
### Panopto API with Python (Organizing Folders)

### Goals:
* Automate organizing folders


#### Features:
* Pull into CSV file



#### Usage examples:
Run the following from terminal from directory .../panoptoAPI/folders

-----Demo-----
(CSV Files)
python3 sample.py ...


Automated Scheduling Test
|
v
CSV 0 of Complete mapping of courses to parent folders

UBC Sauder
|
v
CSV 1 of Parent Folder Ids (Destination)

Sauder
|
v
CSV 2 of child Folder Ids (Origin)

CSV 1 and CSV 2 are used to produce similarity measure between
text of course names (strings), this produces a CSV of 
child folders pointing to the correct parent folder Ids

This final CSV is handed off to the Panopto API where the 
assignment of the correct (destination) parent folder IDs occurs
for all the 144 child folders.

----------------------------------------
### Panopto API with Python (Creating Empty Sessions)

### Goals:
* Auto-upload and create empty sessions
* Download links from generated empty sessions


#### Features:
* Input from CSV file (Completed)
  
* Input from Excel file (Completed, Not yet tested)

    * Input file specification (Completed, Not yet tested)

* Choose destination folder (Completed, Not yet tested)

* Specifiy panopto folder (Completed, Not yet tested)

* User specification (Completed, Not yet tested)

* Input data validation (Partially completed)



#### Usage examples:
Run the following from terminal from directory .../panoptoAPI/folders

-----Demo-----
(CSV Files)
python3 main.py --filePath csvFiles/inputCSV.csv --folderID a7b9e02b-3f0e-4121-b078-ad1600fdaa91 --username <username> --password <password> --fileType csv

(Excel Files)
python3 main.py --filePath excelFiles/inputCSV.xlsx --folderID a7b9e02b-3f0e-4121-b078-ad1600fdaa91 --username <username> --password <password> --fileType xlsx --row 2 --col B --sheet inputCSV

Note: currently both ways output to same file (outputCSV.csv)
