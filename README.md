### Panopto API with Python

### Goals:
* Auto-upload and create empty sessions
* Download links from generated empty sessions


#### Features:
* Input from CSV file (Completed)
  
* Input from Excel file (Partially completed)

    * Input file specification (Partially completed)

* Choose destination folder (Not yet completed)

* Specifiy panopto folder (Future feature)

* User specification (Future feature)

* Input data validation (Future feature)



#### Usage examples:
Run the following from terminal from directory .../panoptoAPI/folders

To input from CSV file:
python3 main.py --filePath csvFiles/inputCSV.csv

To input from Excel file:
python3 mainExcel.py --fileLocation excelFiles/inputCSV.xlsx --sheet inputCSV --col B --row 2

Note: currently both ways output to same file (outputCSV.csv)