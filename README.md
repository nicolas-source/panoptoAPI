### Panopto API with Python

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