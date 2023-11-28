import os

from python_helpers.ph_util import PhUtil

from src.main.excelPlay import process_input

input_items_list = [
    r"..\sample_data\Excel Worksheet1.xlsx",
    r"..\sample_data",
    r"D:\Other\Github_Self\excelPlay\sample_data\Excel Worksheet1.xlsx",
    r"D:\Other\Github_Self\excelPlay\sample_data",
    r"D:\\Other\\Github_Self\\excelPlay\\sample_data\\Excel Worksheet1.xlsx",
    r"D:/Other/Github_Self/excelPlay/sample_data/Excel Worksheet1.xlsx",
]


def main():
    """

    :return:
    """
    for index, input_item in enumerate(input_items_list):
        out_folder_path = os.sep.join([PhUtil.path_default_log_folder, f'TC_{index}'])
        process_input(input_file_or_folder=input_item, output_parent_folder=out_folder_path)


if __name__ == '__main__':
    main()
