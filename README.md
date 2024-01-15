# excelPlay
Export one or more Excel file(s) with single or multiple sheets to several files each containing one sheet.
<BR>All sheets will be exported inside a directory with the same name as of file. 

[![GitHub License](https://img.shields.io/github/license/impratikjaiswal/excelPlay)](LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

[![GitHub Release](https://img.shields.io/github/v/release/impratikjaiswal/excelPlay)](https://github.com/impratikjaiswal/excelPlay/releases/latest)
[![GitHub commits since latest release](https://img.shields.io/github/commits-since/impratikjaiswal/excelPlay/latest)](https://github.com/impratikjaiswal/excelPlay/commits/main/)

[![Static Badge](https://img.shields.io/badge/amenitypj.in/excelPlay-a?label=website%20url)](https://amenitypj.in/excelPlay)
[![Website](https://img.shields.io/website?url=https://amenitypj.in/excelPlay&label=website%20status)](https://amenitypj.in/excelPlay)

[![Static Badge](https://img.shields.io/badge/impratikjaiswal.github.io/excelPlay-a?label=gihub%20website%20url)](https://impratikjaiswal.github.io/excelPlay)
[![Website](https://img.shields.io/website?url=https://amenitypj.in/excelPlay&label=website%20status)](https://impratikjaiswal.github.io/excelPlay)

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
`python -m src.main.excelPlay file_path` OR `excelPlay.exe file_path`
    ```
    Examples:
    
    python -m src.main.excelPlay "test\Excel Worksheet1.xlsx"
    python -m src.main.excelPlay "test"
    python -m src.main.excelPlay "D:\Other\Github_Self\excelPlay\test\Excel Worksheet1.xlsx"
    python -m src.main.excelPlay "D:\Other\Github_Self\excelPlay\test"
    python -m src.main.excelPlay "D:\\Other\\Github_Self\\excelPlay\\test\\Excel Worksheet1.xlsx"
    python -m src.main.excelPlay "D:/Other/Github_Self/excelPlay/test/Excel Worksheet1.xlsx"
    ```
2. Mandatory Parameter: source file or folder path
    ```
    Examples:
    
    python -m src.main.excelPlay file_path
    python -m src.main.excelPlay dir_path
    ```
3. Optional Parameter: target format (csv or xlsx)
    ```
    Examples:
    
    python -m src.main.excelPlay file_path -f csv
    python -m src.main.excelPlay file_path -f xlsx
    ```
4. Optional Parameter: Output Parent Folder path
    ```
    Examples:
    
    python -m src.main.excelPlay file_path -o Test
    ```
