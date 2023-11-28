import os

import click
import pandas as pd
from python_helpers.ph_util import PhUtil

from src.main.helper.constants_config import ConfigConst
from src.main.helper.defaults import Defaults
from src.main.helper.formats import Formats

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def get_sheets(input_file_or_folder, target_file_format, output_parent_folder=None):
    is_dir = True if os.path.isdir(input_file_or_folder) else False
    include_files = [item for item in Formats.SUPPORTED_FORMATS if item not in [target_file_format]]
    include_files = [f'*.{item}' for item in include_files]
    if is_dir:
        files_list = PhUtil.traverse_it(top=input_file_or_folder, include_files=include_files)
    else:
        files_list = [input_file_or_folder]
    if output_parent_folder is None:
        output_parent_folder = ''
    for file_path in files_list:
        folder_path = PhUtil.get_file_name_and_extn(file_path=file_path, path_with_out_extn=True)
        file_name = PhUtil.get_file_name_and_extn(file_path=file_path, name_with_out_extn=True)
        if output_parent_folder:
            folder_path = os.sep.join([output_parent_folder, file_name])
        PhUtil.makedirs(folder_path)
        df1 = pd.ExcelFile(file_path)
        PhUtil.print_separator(main_text=file_path)
        for x in df1.sheet_names:
            print(f'{x}.{target_file_format} Done.')
            df2 = pd.read_excel(file_path, sheet_name=x, dtype='str', na_filter=False)
            filename = os.path.join(folder_path, x + '.' + target_file_format)
            if target_file_format == Formats.CSV:
                df2.to_csv(filename, index=False)
            else:
                df2.to_excel(filename, index=False)
    PhUtil.print_done()


def process_input(input_file_or_folder, target_file_format=Defaults.DEFAULT_FORMAT, output_parent_folder=None):
    if not os.path.exists(input_file_or_folder):
        raise FileNotFoundError(f'Invalid Path: {input_file_or_folder}')
    get_sheets(input_file_or_folder, target_file_format, output_parent_folder)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_file_or_folder')
@click.option('-f', '--target_file_format', type=click.Choice(Formats.SUPPORTED_FORMATS),
              default=Defaults.DEFAULT_FORMAT, help=f'{Defaults.DEFAULT_FORMAT} is Default')
@click.option('-o', '--output_parent_folder', help='Output Parent Folder path')
def cli(input_file_or_folder, target_file_format, output_parent_folder):
    """

    :param input_file_or_folder:
    :param target_file_format:
    :return:
    """
    process_input(input_file_or_folder, target_file_format, output_parent_folder)


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
