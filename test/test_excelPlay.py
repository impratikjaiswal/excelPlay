import os

from python_helpers.ph_util import PhUtil

from excel_play.main.excelPlay import process_input
from excel_play.main.helper.formats import Formats

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

input_items_list_zip = [
    f"{os.sep.join([PhUtil.path_default_log_folder, 'TC_zip_0'])}",
    f"{os.sep.join([PhUtil.path_default_log_folder, 'TC_zip_1'])}",
]


def main():
    """

    :return:
    """
    PhUtil.print_heading(str_heading='input_items_list_w_output_folder')
    for index, input_item in enumerate(input_items_list_w_output_folder):
        out_folder_path = os.sep.join([PhUtil.path_default_log_folder, f'TC_{index}'])
        output_files_list = process_input(input_file_or_folder=input_item, output_parent_folder=out_folder_path)
        PhUtil.print_iter(output_files_list, header='output_files_list')

    PhUtil.print_heading(str_heading='input_items_list_wo_output_folder')
    for index, input_item in enumerate(input_items_list_wo_output_folder):
        output_files_list = process_input(input_file_or_folder=input_item)
        PhUtil.print_iter(output_files_list, header='output_files_list')

    PhUtil.print_heading(str_heading='input_items_list_zip')
    for index, input_item in enumerate(input_items_list_zip):
        output_files_list = process_input(input_file_or_folder=input_item, output_archive_format=Formats.ZIP)
        PhUtil.print_iter(output_files_list, header='output_files_list')

    PhUtil.print_heading(str_heading='input_items_list_multi')
    output_files_list = process_input(input_file_or_folder=input_items_list_w_output_folder, output_archive_format=Formats.ZIP)
    PhUtil.print_iter(output_files_list, header='output_files_list')

if __name__ == '__main__':
    main()
