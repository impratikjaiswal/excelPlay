from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_util import PhUtil


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
        PhKeys.VAR_EXECUTION_MODE: 'ALL',
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
                PhKeys.BATCH_PARAMS: 'D:\Other\Github_Self\excelPlay\data\sampleData\Excel Worksheet2.xlsx',
            },
        'input_file_2':
            {
                PhKeys.BATCH_PARAMS: r'"D:\Other\Github_Self\excelPlay\data\sampleData\Excel Worksheet2.xlsx"',
            },
    }

    read_me_cli_pool = [
        "file_path",
        "data\sampleData\Excel Worksheet1.xlsx",
        "data\sampleData\Excel Worksheet1.xlsx" "data\sampleData\Excel Worksheet2.xlsx",
        "data\sampleData",
        "D:\Other\Github_Self\excelPlay\data\sampleData\Excel Worksheet1.xlsx",
        "D:\Other\Github_Self\excelPlay\data\sampleData",
        "D:\\Other\\Github_Self\\excelPlay\\data\sampleData\\Excel Worksheet1.xlsx",
        "D:/Other/Github_Self/excelPlay/data/sampleData/Excel Worksheet1.xlsx",
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
    def get_test_data(cls, key):
        dynamic_data = cls.dynamic_data.get(key, PhConstants.DICT_EMPTY)
        key_name = PhExecutionModes.get_key_name(key) if key in PhExecutionModes.KEYS_NAME else key
        for temp_key in cls.default_data:
            if temp_key not in dynamic_data:
                dynamic_data[temp_key] = cls.default_data[temp_key]
        static_data = {
            PhKeys.TEST_CASE_ID: key_name,
            PhKeys.TEST_CASE_NAME: key_name,
            PhKeys.TEST_CASE_FILE_NAME: f'{key_name}.log'
        }
        return PhUtil.dict_merge(static_data, dynamic_data)

    @classmethod
    def get_test_data_cli(cls, key):
        key_name = 'cli_' + key
        dynamic_data = cls.dynamic_data_cli.get(key, PhConstants.DICT_EMPTY)
        static_data = {
            PhKeys.TEST_CASE_ID: key_name,
            PhKeys.TEST_CASE_NAME: key_name,
            PhKeys.TEST_CASE_FILE_NAME: f'{key_name}.log'
        }
        return PhUtil.dict_merge(static_data, dynamic_data)

    @classmethod
    def generate_dynamic_cli_from_read_me(cls):
        for index, batch_param in enumerate(TestData.read_me_cli_pool):
            TestData.dynamic_data_cli.update({f'read_me_{index}': {PhKeys.BATCH_PARAMS: f'"{batch_param}"'}})