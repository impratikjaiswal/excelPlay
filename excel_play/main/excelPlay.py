import os

import click
import pandas as pd
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil

from excel_play.main.helper.constants_config import ConfigConst
from excel_play.main.helper.defaults import Defaults
from excel_play.main.helper.formats import Formats

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def process_files(files_list, target_file_format, output_parent_folder, output_archive_format, output_encoding,
                  output_encoding_error_handling):
    output_files_list = []
    for file_path in files_list:
        folder_path = PhUtil.get_file_name_and_extn(file_path=file_path, path_with_out_extn=True)
        folder_path = PhUtil.append_in_file_name(str_file_path=folder_path, str_append=ConfigConst.TOOL_NAME,
                                                 file_path_is_dir=True, treat_folder_as_file=True)
        file_name = PhUtil.get_file_name_and_extn(file_path=file_path, name_with_out_extn=True)
        if output_parent_folder:
            folder_path = os.sep.join([output_parent_folder, file_name])
        PhUtil.makedirs(folder_path)
        df1 = pd.ExcelFile(file_path)
        PhUtil.print_separator(main_text=file_path)
        print(f'out_put_path: {folder_path}')
        output_files_list_single_file = []
        for x in df1.sheet_names:
            df2 = pd.read_excel(file_path, sheet_name=x, dtype='str', na_filter=False)
            filename = os.path.join(folder_path, x + '.' + target_file_format)
            status = 'Done.'
            try:
                if target_file_format == Formats.CSV:
                    df2.to_csv(filename, index=False, encoding=output_encoding, errors=output_encoding_error_handling)
                else:
                    df2.to_excel(filename, index=False)
            except Exception as e:
                status = 'Failed.'
            output_files_list_single_file.append(filename)
            print(f'{x}.{target_file_format} {status}')
        if output_archive_format:
            if output_archive_format == Formats.ZIP:
                zip_file_path = PhUtil.zip_and_clean_dir(source_files_dir=folder_path,
                                                         delete_dir_after_zip=False,
                                                         export_hash=False)
            output_files_list_single_file = [zip_file_path]
            output_files_list += output_files_list_single_file
        else:
            output_files_list += output_files_list_single_file
    return output_files_list


def get_sheets(input_files_or_folders, target_file_format, output_parent_folder=None, output_archive_format=None,
               output_encoding=None, output_encoding_error_handling=None):
    """

    :param input_files_or_folders:
    :param target_file_format:
    :param output_parent_folder:
    :param output_archive_format:
    :param output_encoding:
    :param output_encoding_error_handling:
    :return:
    """
    output_files_or_folders = []
    multiple_files = True if (
        # CUI Multi
            isinstance(input_files_or_folders, tuple)
            or
            # Web App Multi
            isinstance(input_files_or_folders, list)
    ) else False
    if not multiple_files:
        input_files_or_folders = [input_files_or_folders]
    output_encoding = PhUtil.set_if_empty(output_encoding, Defaults.DEFAULT_ENCODING_FORMAT)
    output_encoding_error_handling = PhUtil.set_if_empty(output_encoding_error_handling,
                                                         Defaults.DEFAULT_ENCODING_ERROR_HANDLING)
    for input_file_or_folder in input_files_or_folders:
        if not os.path.exists(input_file_or_folder):
            raise FileNotFoundError(f'Invalid Path: {input_file_or_folder}')
        is_dir = True if os.path.isdir(input_file_or_folder) else False
        include_files = [item for item in Formats.SUPPORTED_FORMATS if item not in [target_file_format]]
        include_files = [f'*.{item}' for item in include_files]
        if is_dir:
            files_list = PhUtil.traverse_it(top=input_file_or_folder, include_files=include_files)
        else:
            files_list = [input_file_or_folder]
        output_parent_folder = PhUtil.set_if_none(output_parent_folder)
        output_file_or_folder = process_files(
            files_list=files_list,
            target_file_format=target_file_format,
            output_parent_folder=output_parent_folder,
            output_archive_format=output_archive_format,
            output_encoding=output_encoding,
            output_encoding_error_handling=output_encoding_error_handling
        )
        output_files_or_folders = output_files_or_folders + output_file_or_folder
    PhUtil.print_done()
    return output_files_or_folders


def process_input(input_file_or_folder, target_file_format=Defaults.DEFAULT_FORMAT, output_parent_folder=None,
                  output_archive_format=None, print_version=True, output_encoding=None,
                  output_encoding_error_handling=None):
    if print_version is True:
        # Print Versions
        PhUtil.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION)
    return get_sheets(input_files_or_folders=input_file_or_folder, target_file_format=target_file_format,
                      output_parent_folder=output_parent_folder, output_archive_format=output_archive_format,
                      output_encoding=output_encoding, output_encoding_error_handling=output_encoding_error_handling)


@click.command(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)
@click.argument('input_file_or_folder', nargs=-1)
@click.option('-f', '--target_file_format', type=click.Choice(Formats.SUPPORTED_FORMATS),
              default=Defaults.DEFAULT_FORMAT, help=f'{Defaults.DEFAULT_FORMAT} is Default')
@click.option('-o', '--output_parent_folder', help='Output Parent Folder path')
@click.option('-a', '--output_archive_format', type=click.Choice(Formats.SUPPORTED_ARCHIVE_FORMATS),
              default=Defaults.DEFAULT_ARCHIVE_FORMAT,
              help=f'Archive Format (if Archive/Single File is needed); {Defaults.DEFAULT_ARCHIVE_FORMAT} is Default')
@click.option('-e', '--output_encoding', type=click.Choice(PhConstants.STR_ENCODING_FORMAT_POOL),
              default=Defaults.DEFAULT_ENCODING_FORMAT,
              help=f'Output Data Encoding; {Defaults.DEFAULT_ENCODING_FORMAT} is Default')
@click.option('-ee', '--output_encoding_error_handling',
              type=click.Choice(PhConstants.STR_ENCODING_ERROR_HANDLING_POOL),
              default=Defaults.DEFAULT_ENCODING_ERROR_HANDLING,
              help=f'Output Data Encoding Error Handling; {Defaults.DEFAULT_ENCODING_ERROR_HANDLING} is Default')
def cli(input_file_or_folder, target_file_format, output_parent_folder, output_archive_format, output_encoding,
        output_encoding_error_handling):
    """

    :param input_file_or_folder:
    :param target_file_format:
    :param output_parent_folder:
    :param output_archive_format:
    :param output_encoding:
    :param output_encoding_error_handling:
    :return:
    """
    process_input(input_file_or_folder=input_file_or_folder, target_file_format=target_file_format,
                  output_parent_folder=output_parent_folder, print_version=False,
                  output_archive_format=output_archive_format, output_encoding=output_encoding,
                  output_encoding_error_handling=output_encoding_error_handling)


def main():
    """

    :return:
    """
    # Print Versions
    PhUtil.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION)
    # Process Data
    cli()
    PhUtil.print_done()


if __name__ == '__main__':
    main()
