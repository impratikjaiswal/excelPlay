from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_execution import PhExecutionModes


class TestData:
    # Unit Testing Sequences
    dynamic_data = {
        PhExecutionModes.UNIT_TESTING:
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING',
            },
        PhExecutionModes.USER:
            {
                PhKeys.VAR_EXECUTION_MODE: 'USER',
            },
        PhExecutionModes.SAMPLES_LIST:
            {
                PhKeys.VAR_EXECUTION_MODE: 'SAMPLES_LIST',
            },
        PhExecutionModes.DEV:
            {
                PhKeys.VAR_EXECUTION_MODE: 'DEV',
            },
        PhExecutionModes.KNOWN_ISSUES:
            {
                PhKeys.VAR_EXECUTION_MODE: 'KNOWN_ISSUES',
            },
        PhExecutionModes.UNIT_TESTING_EXTERNAL:
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING_EXTERNAL',
            },
        PhExecutionModes.ALL:
            {
                PhKeys.VAR_EXECUTION_MODE: 'ALL',
            },
    }

    default_data = {
        PhKeys.VAR_EXECUTION_MODE: 'USER',
        PhKeys.VAR_ERROR_HANDLING_MODE: 'CONTINUE_ON_ERROR',
        PhKeys.VAR_TOP_FOLDER_PATH: '[]',
    }

    #
    dynamic_data_cli = {
        'no_param':
            {
                PhKeys.BATCH_PARAMS: '',
            },
        '--help':
            {
                PhKeys.BATCH_PARAMS: '--help',
            },
        'input_file_1':
            {
                PhKeys.BATCH_PARAMS: 'D:\Other\Github_Self\excelPlay\data\sample_data\Excel Worksheet2.xlsx',
            },
        'input_file_2':
            {
                PhKeys.BATCH_PARAMS: r'"D:\Other\Github_Self\excelPlay\data\sample_data\Excel Worksheet2.xlsx"',
            },
    }

    read_me_cli_pool = [
        "file_path",
        "data\sample_data\Excel Worksheet1.xlsx",
        "data\sample_data\Excel Worksheet1.xlsx" "data\sample_data\Excel Worksheet2.xlsx",
        "data\sample_data",
        "D:\Other\Github_Self\excelPlay\data\sample_data\Excel Worksheet1.xlsx",
        "D:\Other\Github_Self\excelPlay\data\sample_data",
        "D:\\Other\\Github_Self\\excelPlay\\data\sample_data\\Excel Worksheet1.xlsx",
        "D:/Other/Github_Self/excelPlay/data/sample_data/Excel Worksheet1.xlsx",
        "file_path",
        "dir_path",
        "file_path -f .csv",
        "file_path --output_format .csv",
        "file_path -f .xlsx",
        "file_path -ff .zip",
        "file_path --archive_output_format .zip",
        "file_path -a False",
        "file_path --archive_output True",
        "file_path --archive_output true",
        "file_path --archive_output yes",
        "file_path -o Test",
        "file_path --output_path Test",
        "file_path -e ascii",
        "file_path --encoding ascii",
        "file_path -ee replace",
        "file_path --encoding_errors replace",
        "--help",
    ]

    @classmethod
    def generate_dynamic_cli_from_read_me(cls):
        for index, batch_param in enumerate(TestData.read_me_cli_pool):
            TestData.dynamic_data_cli.update({f'read_me_{index}': {PhKeys.BATCH_PARAMS: f'"{batch_param}"'}})
