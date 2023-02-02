# excelPlay
Export one or more Excel file(s) with single or multiple sheets to several files each containing one sheet.
<BR>All sheets will be exported inside a directory with the same name as of file. 

# How To Install 
<ol>
    <li>All Required packages are listed in requirements.txt
    <li>Few Basic Scripts are also present under <i>scripts</i> folder.
        <ol>
            <li>Currently Scripts are targeting virtual environment with folder name as <i>.venv</i> (Present in parallel of <i>scripts</i> folder)
            <li>However, same can be modified as per user choice. 
        </ol>
</ol>

    Note: installing tool in virtual environment is optional but preferred.

# Sample Usage
<ol>
    <li>Run form command prompt or via IDE or via executable (Executable needs to generate separately) 
    <ul>
        <li>python -m src.main.excelPlay file_path
        <li>excelPlay.exe file_path
    </ul>
    <ul>
        <li>python -m src.main.excelPlay "test\Excel Worksheet1.xlsx"
        <li>python -m src.main.excelPlay "test"
        <li>python -m src.main.excelPlay "D:\Other\Github_Self\excelPlay\test\Excel Worksheet1.xlsx"
        <li>python -m src.main.excelPlay "D:\Other\Github_Self\excelPlay\test"
        <li>python -m src.main.excelPlay "D:\\Other\\Github_Self\\excelPlay\\test\\Excel Worksheet1.xlsx"
        <li>python -m src.main.excelPlay "D:/Other/Github_Self/excelPlay/test/Excel Worksheet1.xlsx"
    </ul>
    <li>Mandatory Parameter: source file or folder path
    <ul>
        <li>python -m src.main.excelPlay file_path
        <li>python -m src.main.excelPlay dir_path
    </ul>
    <li>Optional Parameter: target format (csv or xlsx) 
    <ul>
        <li>python -m src.main.excelPlay file_path -f csv
        <li>python -m src.main.excelPlay file_path -f xlsx
    </ul>
    <li>Optional Parameter: Output Parent Folder path 
    <ul>
        <li>python -m src.main.excelPlay file_path -o Test
    </ul>
</ol>

# Samples
