import os

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData, PhMasterDataKeys
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_file_extensions import PhFileExtensions
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from excel_play.main.helper.data import Data
from excel_play.main.helper.defaults import Defaults
from excel_play.main.helper.formats import Formats
from excel_play.main.helper.formats_group import FormatsGroup
from excel_play.main.helper.keywords import KeyWords


def print_data(data=None, meta_data=None, info_data=None, master_data=None):
    """
    
    :param data:
    :param meta_data:
    :param info_data:
    :param master_data:
    :return:
    """
    if master_data is not None and isinstance(master_data, PhMasterData):
        data = master_data.get_master_data(PhMasterDataKeys.DATA)
        meta_data = master_data.get_master_data(PhMasterDataKeys.META_DATA)
        info_data = master_data.get_master_data(PhMasterDataKeys.INFO_DATA)
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE
    if data.print_info:
        remarks_original = data.get_remarks_as_str(user_original_remarks=True)
        remarks_generated = data.get_remarks_as_str()
        remarks_generated_stripping_needed = True if remarks_generated.endswith(
            PhConstants.DEFAULT_TRIM_STRING) else False
        if remarks_original:
            if remarks_generated_stripping_needed:
                if remarks_generated.strip(PhConstants.DEFAULT_TRIM_STRING) in remarks_original:
                    remarks_generated = ''
            else:
                if remarks_original in remarks_generated:
                    remarks_generated = ''
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                              remarks_generated))
        if info_data is not None:
            info_count = info_data.get_info_count()
            info_msg = info_data.get_info_str()
            if info_msg:
                sep = PhConstants.SEPERATOR_MULTI_LINE_TABBED if info_count > 1 else PhConstants.SEPERATOR_ONE_LINE
                meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.INFO_DATA, sep, info_msg))
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            PhUtil.get_dic_data_and_print(PhKeys.TRANSACTION_ID, PhConstants.SEPERATOR_ONE_LINE,
                                          meta_data.transaction_id, dic_format=False, print_also=False),
            PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.output_format,
                                          dic_format=False, print_also=False) if data.output_format else None,
            PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_PATH, PhConstants.SEPERATOR_ONE_LINE, data.output_path,
                                          dic_format=False, print_also=False) if data.output_path else None,
            PhUtil.get_dic_data_and_print(PhKeys.ENCODING, PhConstants.SEPERATOR_ONE_LINE, data.encoding,
                                          dic_format=False, print_also=False) if data.encoding else None,
            PhUtil.get_dic_data_and_print(PhKeys.ENCODING_ERRORS, PhConstants.SEPERATOR_ONE_LINE, data.encoding_errors,
                                          dic_format=False, print_also=False) if data.encoding_errors else None,
            PhUtil.get_dic_data_and_print(PhKeys.ARCHIVE_OUTPUT, PhConstants.SEPERATOR_ONE_LINE, data.archive_output,
                                          dic_format=False, print_also=False) if data.archive_output else None,
            PhUtil.get_dic_data_and_print(PhKeys.ARCHIVE_OUTPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE,
                                          data.archive_output_format,
                                          dic_format=False, print_also=False) if data.archive_output_format else None,
            PhUtil.get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                          dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
    if data.print_input:
        meta_data.output_dic.update(
            PhUtil.get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, meta_data.input_data_org))
    output_present = meta_data.parsed_data
    print_output = data.print_output
    if data.print_output and print_output:  # and meta_data.parsed_data:
        res = '\n'.join(PhUtil.to_list(meta_data.parsed_data))
        meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, res))
    PhUtil.print_separator()


def set_includes_excludes_files(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    # TODO: Revisit this
    include_files = [item for item in FormatsGroup.FILE_FORMATS_SUPPORTED if item not in [data.output_format]]
    include_files = [f'*{item}' for item in include_files]
    meta_data.include_files = include_files
    # Always exclude output files
    meta_data.excludes = ['*_' + KeyWords.OUTPUT_FILE_NAME_KEYWORD + '.*']
    # Include Everything for now


def parse_config(config_data):
    data_types = {
    }
    config_data = PhUtil.parse_config(config_data, data_types=data_types)
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if not v:
            continue
        config_data[k] = v
    # PhUtil.print_iter(config_data, 'config_data before cleaning', verbose=True, depth_level=1)
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def set_defaults_for_common_objects(data):
    """

    :param data:
    :return:
    """
    data.quite_mode = PhUtil.set_if_none(data.quite_mode, Defaults.QUITE_MODE)
    data.print_input = PhUtil.set_if_none(data.print_input, Defaults.PRINT_INPUT)
    data.print_output = PhUtil.set_if_none(data.print_output, Defaults.PRINT_OUTPUT)
    data.print_info = PhUtil.set_if_none(data.print_info, Defaults.PRINT_INFO)
    data.encoding = PhUtil.set_if_none(data.encoding, Defaults.ENCODING)
    data.encoding_errors = PhUtil.set_if_none(data.encoding_errors, Defaults.ENCODING_ERRORS)
    data.archive_output = PhUtil.set_if_none(data.archive_output, Defaults.ARCHIVE_OUTPUT)
    data.archive_output_format = PhUtil.set_if_none(data.archive_output_format, Defaults.ARCHIVE_OUTPUT_FORMAT)


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    data.output_format = PhUtil.set_if_none(data.output_format, Defaults.OUTPUT_FORMAT)
    data.output_path = PhUtil.set_if_none(data.output_path, Defaults.OUTPUT_PATH)
    if meta_data is None:
        return


def read_web_request(request_form):
    return Data(**parse_config(request_form))


def set_output_file_path(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    remarks = data.get_remarks_as_str()
    meta_data.file_based = True if data.image_format in [Formats.PNG, Formats.SVG] else False
    if meta_data.file_based:
        meta_data.output_file = os.sep.join(
            [PhUtil.path_default_out_folder, PhUtil.get_python_friendly_name(remarks if remarks else 'qr_code')])
        meta_data.output_file = PhUtil.append_in_file_name(meta_data.output_file,
                                                           new_ext=PhFileExtensions.SVG if data.image_format == Formats.SVG else PhFileExtensions.PNG)
        PhUtil.make_dirs(PhUtil.get_file_name_and_extn(meta_data.output_file, only_path=True))


def read_input_file(data, meta_data, info_data):
    try:
        # Text File
        with open(data.input_data, mode='r', encoding=data.encoding, errors=data.encoding_errors) as the_file:
            resp = ''.join(the_file.readlines())
    except UnicodeDecodeError:
        # Binary File/Encoding Error
        with open(data.input_data, 'rb') as the_file:
            resp = the_file.read()
    if not resp:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.EMPTY_INPUT_FILE))
    return resp


def write_output_file(data, meta_data, info_data, flip_output=False):
    output_file_path = meta_data.output_file_path
    data_to_write = meta_data.parsed_data
    if flip_output is True:
        output_file_path = meta_data.re_output_file_path
        data_to_write = meta_data.re_parsed_data
    data_to_write = PhUtil.set_if_none(data_to_write, PhConstants.STR_EMPTY)
    with open(output_file_path, mode='w', encoding=data.encoding, errors=data.encoding_errors) as file:
        file.writelines(data_to_write)
