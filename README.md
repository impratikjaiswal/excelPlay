# excelPlay
Split Microsoft Excel file to multiple CSV file(s). One CSV File will contain one sheet. 
<BR>Multiple input files can be provided in one shot.

[![GitHub License](https://img.shields.io/github/license/impratikjaiswal/excelPlay)](LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

[![GitHub Release](https://img.shields.io/github/v/release/impratikjaiswal/excelPlay)](https://github.com/impratikjaiswal/excelPlay/releases/latest)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/impratikjaiswal/excelPlay/latest)](https://github.com/impratikjaiswal/excelPlay/commits/main/)

[![Static Badge](https://img.shields.io/badge/amenitypj.in/excelPlay-a?label=website%20url)](https://amenitypj.in/excelPlay)
[![Website](https://img.shields.io/website?url=https://amenitypj.in/excelPlay&label=website%20status)](https://amenitypj.in/excelPlay)

[![Static Badge](https://img.shields.io/badge/impratikjaiswal.github.io/excelPlay-a?label=gihub%20website%20url)](https://impratikjaiswal.github.io/excelPlay)
[![Website](https://img.shields.io/website?url=https://impratikjaiswal.github.io/excelPlay&label=website%20status)](https://impratikjaiswal.github.io/excelPlay)

# Url(s) of AmenityPj 
Refer [Url(s) of AmenityPj](https://impratikjaiswal.github.io/amenitypj/#urls-of-amenitypj) for details.

# Screen Shot(s) of Web App [![Static Badge](https://img.shields.io/badge/amenitypj.in-a)](https://amenitypj.in/) 
![sample_web_1](https://github.com/impratikjaiswal/excelPlay/blob/main/static/images/sample_web_1.gif?raw=true)

# Installation/Setup
Steps can be found [here](https://github.com/impratikjaiswal/pythonHelpers/blob/main/HOW_TO_INSTALL_PYTHON_APPS.md).

# How To Use
There are various ways to Get Started:

  - Online Mode
    - Website [![Static Badge](https://img.shields.io/badge/amenitypj.in-a)](https://amenitypj.in/) can be used
  - Offline Mode (Requires Download / Cloning of the Repo)
    - Code can be directly run from ```excelPlay/excel_play/main/excelplay.py``` using any IDE (Parameter can be passed via IDE)
    - Local Web Server App [amenitypj](https://github.com/impratikjaiswal/amenitypj) can be used

# Help
Issue tracker can be found [here](CONTRIBUTING.md#issue-tracker).

# Contributing
 - Code of Conduct can be found [here](CODE_OF_CONDUCT.md).
 - Contributing Guidelines can be found [here](CONTRIBUTING.md).

# Sample Usage
1. Run form command prompt or via IDE or via executable (Executable needs to generate separately) 
`python -m excel_play.main.excelPlay file_path` OR `excelPlay.exe file_path`
    ```
    Examples:
    
    python -m excel_play.main.excelPlay "sample_data\Excel Worksheet1.xlsx"
    python -m excel_play.main.excelPlay "sample_data\Excel Worksheet1.xlsx" "sample_data\Excel Worksheet2.xlsx"
    python -m excel_play.main.excelPlay "sample_data"
    python -m excel_play.main.excelPlay "D:\Other\Github_Self\excelPlay\sample_data\Excel Worksheet1.xlsx"
    python -m excel_play.main.excelPlay "D:\Other\Github_Self\excelPlay\sample_data"
    python -m excel_play.main.excelPlay "D:\\Other\\Github_Self\\excelPlay\\sample_data\\Excel Worksheet1.xlsx"
    python -m excel_play.main.excelPlay "D:/Other/Github_Self/excelPlay/sample_data/Excel Worksheet1.xlsx"
    ```
2. Mandatory Parameter: source file or folder path
    ```
    Examples:
    
    python -m excel_play.main.excelPlay file_path
    python -m excel_play.main.excelPlay dir_path
    ```
3. Optional Parameter: target format (csv or xlsx)
    ```
    Examples:
    
    python -m excel_play.main.excelPlay file_path -f csv
    python -m excel_play.main.excelPlay file_path -f xlsx
    ```
4. Optional Parameter: Output Parent Folder path
    ```
    Examples:
    
    python -m excel_play.main.excelPlay file_path -o Test
    ```

5. Help
    ```
    python -m excel_play.main.excelPlay -h
    ```
