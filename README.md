# excelPlay
Export one or more Excel file(s) with single or multiple sheets to several files each containing one sheet.
<BR>All sheets will be exported inside a directory with the same name as of file. 

# How To Install

1. All Required packages are listed in requirements.txt
1. Few Basic Scripts are also present under <i>scripts</i> folder.
   - Currently, Scripts are targeting virtual environment with folder name as <i>venv</i> (Present in parallel of <i>scripts</i> folder)
   - However, same can be modified as per user choice.
   
    **Note:** installing tool in virtual environment is optional but preferred.

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
