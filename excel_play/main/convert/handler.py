import os

import pandas as pd
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_util import PhUtil

from excel_play.main.helper.constants_config import ConfigConst
from excel_play.main.helper.formats import Formats


def handle_data(data, meta_data, info_data, flip_output=False):
    """

    :param data:
    :param meta_data:
    :param info_data:
    :param flip_output:
    :return:
    """
    input_data = data.input_data
    # input_File_path = meta_data.input_data_org if meta_data.input_mode_key == PhKeys.INPUT_FILE else None
    # input_format = data.input_format
    # output_format = data.output_format
    # if flip_output is True:
    #     input_data = meta_data.parsed_data
    #     input_format = data.output_format
    #     output_format = data.input_format
    # parse_only = True
    # asn1_element = data.asn1_element
    if not data.input_data:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.MISSING_INPUT_DATA))
    if not os.path.exists(data.input_data):
        raise FileNotFoundError(f'Invalid Path: {data.input_data}')
    res = __handle_data(data=data, meta_data=meta_data, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res


def __handle_data(data, meta_data, info_data):
    info_data_available = False if PhUtil.is_none(info_data) else True
    file_path = data.input_data
    output_parent_folder = data.output_path
    archive_output = data.archive_output
    output_files_list = []
    #
    folder_path = PhUtil.get_file_name_and_extn(file_path=file_path, path_with_out_extn=True)
    folder_path = PhUtil.append_in_file_name(str_file_path=folder_path, str_append=ConfigConst.TOOL_NAME,
                                             file_path_is_dir=True, treat_folder_as_file=True)
    file_name = PhUtil.get_file_name_and_extn(file_path=file_path, name_with_out_extn=True)
    if output_parent_folder:
        folder_path = os.sep.join([output_parent_folder, file_name])
    PhUtil.make_dirs(folder_path, quite_mode=False)
    df1 = pd.ExcelFile(file_path)
    PhUtil.print_separator(main_text=file_path)
    print(f'out_put_path: {folder_path}')
    output_files_list_single_file = []
    for x in df1.sheet_names:
        df2 = pd.read_excel(file_path, sheet_name=x, dtype='str', na_filter=False)
        dest_file_name = f'{x}.{data.output_format}'
        dest_file_path = os.path.join(folder_path, dest_file_name)
        status = 'Done.'
        try:
            if data.output_format == Formats.CSV:
                df2.to_csv(dest_file_path, index=False, encoding=data.encoding, errors=data.encoding_errors)
            else:
                df2.to_excel(dest_file_path, index=False)
        except Exception as e:
            status = 'Failed.'
        output_files_list_single_file.append(dest_file_path)
        if info_data_available:
            info_data.set_info(f'{dest_file_name} {status}')
    if archive_output:
        output_files_list_single_file = [
            PhUtil.archive_files(source_files_dir=folder_path, archive_format=data.archive_output_format,
                                 delete_dir_after_archive=False, export_hash=False)]
        output_files_list += output_files_list_single_file
    else:
        output_files_list += output_files_list_single_file
    return output_files_list
