import os

from python_helpers.ph_util import PhUtil

from excel_play.main.excelPlay import process_input

input_items_list_w_output_folder = [
    r"..\sample_data\Excel Worksheet1.xlsx",
    r"..\sample_data",
    r"D:\Other\Github_Self\excelPlay\sample_data\Excel Worksheet1.xlsx",
    r"D:\Other\Github_Self\excelPlay\sample_data",
    r"D:\\Other\\Github_Self\\excelPlay\\sample_data\\Excel Worksheet1.xlsx",
    r"D:/Other/Github_Self/excelPlay/sample_data/Excel Worksheet1.xlsx",
]

input_items_list_wo_output_folder = [
    f"{os.sep.join([PhUtil.path_default_log_folder, 'TC_wo_out_folder_0'])}",
    f"{os.sep.join([PhUtil.path_default_log_folder, 'TC_wo_out_folder_1'])}",
]


def main():
    """

    :return:
    """
    for index, input_item in enumerate(input_items_list_w_output_folder):
        out_folder_path = os.sep.join([PhUtil.path_default_log_folder, f'TC_{index}'])
        process_input(input_file_or_folder=input_item, output_parent_folder=out_folder_path)

    for index, input_item in enumerate(input_items_list_wo_output_folder):
        process_input(input_file_or_folder=input_item)


if __name__ == '__main__':
    main()
