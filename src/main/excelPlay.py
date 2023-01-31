import os

import click
import pandas as pd
from util_helpers.util import print_done, print_version, print_version_pkg, print_separator, traverse_it, \
    get_file_name_and_extn, makedirs

from src.main.helper.constants_config import ConfigConst
from src.main.helper.defaults import Defaults
from src.main.helper.formats import Formats

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def get_sheets(input_file_or_folder, target_file_format):
    is_dir = True if os.path.isdir(input_file_or_folder) else False
    include_files = [item for item in Formats.SUPPORTED_FORMATS if item not in [target_file_format]]
    include_files = [f'*.{item}' for item in include_files]
    if is_dir:
        files_list = traverse_it(top=input_file_or_folder, include_files=include_files)
    else:
        files_list = [input_file_or_folder]
    for file_path in files_list:
        folder_path = get_file_name_and_extn(file_path=file_path, path_with_out_extn=True)
        makedirs(folder_path)
        df1 = pd.ExcelFile(file_path)
        print_separator(main_text=file_path)
        for x in df1.sheet_names:
            print(f'{x}.{target_file_format} Done.')
            df2 = pd.read_excel(file_path, sheet_name=x, dtype='str', na_filter=False)
            filename = os.path.join(folder_path, x + '.' + target_file_format)
            if target_file_format == 'csv':
                df2.to_csv(filename, index=False)
            else:
                df2.to_excel(filename, index=False)
    print_done()


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('input_file_or_folder')
@click.option('-f', '--target_file_format', type=click.Choice(Formats.SUPPORTED_FORMATS),
              default=Defaults.DEFAULT_FORMAT, help=f'{Defaults.DEFAULT_FORMAT} is Default')
def cli(input_file_or_folder, target_file_format):
    """Convert a Excel file with multiple sheets to several files with one sheet.

    Examples:

    """
    if not os.path.exists(input_file_or_folder):
        raise FileNotFoundError('Invalid Path...')
    get_sheets(input_file_or_folder, target_file_format)


def main():
    """

    :return:
    """
    print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION)
    print_version_pkg(with_python_version=False)
    cli()
    print_done()


if __name__ == '__main__':
    main()
