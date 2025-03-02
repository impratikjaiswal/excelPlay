import os

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_dos import PhDos
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_process import PhProcess
from python_helpers.ph_util import PhUtil

from excel_play import MODULE_NAME, PACKAGE_NAME
from excel_play.main.excelplay import print_configurations
from excel_play.test.test_data import TestData


class TestAutoBatch:
    white_listed_tcs = None

    PROJECT_PATH = r'D:\Other\Github_Self\excelPlay'

    get_file_path_mapping_relative = {
        PhKeys.VAR_EXECUTION_MODE: r'excel_play\main\excelplay.py',
        PhKeys.VAR_ERROR_HANDLING_MODE: r'excel_play\main\excelplay.py',
        PhKeys.VAR_TOP_FOLDER_PATH: r'excel_play\main\helper\folders.py',
    }

    get_target_str = {
        PhKeys.VAR_EXECUTION_MODE: 'execution_mode = PhExecutionModes.',
        PhKeys.VAR_ERROR_HANDLING_MODE: 'error_handling_mode = PhErrorHandlingModes.',
        PhKeys.VAR_TOP_FOLDER_PATH: 'top_folder_path = ',
    }

    @classmethod
    def _update_variables_in_file(cls, test_case_data):

        def __update_variable_in_file(_target_file, _target_str, _target_value):
            update_available = False
            current_value = None
            if PhUtil.is_empty(_target_file):
                return None
            if PhUtil.is_empty(_target_str):
                return None
            if PhUtil.is_empty(_target_value):
                return None
            with open(_target_file) as f_read:
                file_data = f_read.read().split('\n')
            for index, item in enumerate(file_data):
                if _target_str in item:
                    item_data = item.split(_target_str)
                    if len(item_data) > 1:
                        current_value = item_data[1]
                        if PhUtil.is_not_empty(current_value) and _target_value != current_value:
                            update_available = True
                            item_data[1] = _target_value
                        if update_available:
                            file_data[index] = _target_str.join(item_data)
                        break
            if update_available:
                with open(_target_file, 'w') as f_write:
                    f_write.writelines('\n'.join(file_data))
                return current_value
            return None

        original_data = {}
        target_keys = [
            PhKeys.VAR_EXECUTION_MODE,
            PhKeys.VAR_ERROR_HANDLING_MODE,
            PhKeys.VAR_TOP_FOLDER_PATH,
            PhKeys.OUTPUT_FORMAT,
        ]
        for target_key in target_keys:
            if target_key not in test_case_data:
                continue
            target_str = TestAutoBatch.get_target_str.get(target_key)
            target_value = test_case_data.get(target_key)
            target_file = os.sep.join(
                [TestAutoBatch.PROJECT_PATH, TestAutoBatch.get_file_path_mapping_relative.get(target_key)])
            value_original = __update_variable_in_file(target_file, target_str, target_value)
            if value_original is not None:
                print(f'{target_key}: value_original was {value_original}; target_value is {target_value}')
                original_data.update({target_key: value_original})
        return original_data

    @classmethod
    def clean_up(cls, original_data):
        cls._update_variables_in_file(original_data)

    @classmethod
    def prepare_batch_file(cls, test_case_data, default_batch_data=None, batch_params=None):
        """

        :param default_batch_data:
        :param test_case_data:
        :param batch_params:
        :return:
        """
        log_file_path = os.sep.join([PACKAGE_NAME, 'test', 'logs', test_case_data.get(PhKeys.TEST_CASE_FILE_NAME)])
        executable_script = [
            default_batch_data,
            PhDos.echo_off(),
            PhDos.switch_to_current_folder(),
            PhDos.get_seperator(test_case_data.get(PhKeys.TEST_CASE_ID)),
            PhDos.change_directory_parent(),
            PhDos.change_directory_parent(),
            PhDos.create_directory(file_path=log_file_path),
            PhDos.call_script_for_env_handling(True),
            PhConstants.SEPERATOR_TWO_WORDS.join(filter(None, [
                PhDos.run_python(module_name=MODULE_NAME),
                batch_params,
                PhDos.redirect_output(file_path=log_file_path)
            ])),
            PhDos.call_script_for_env_handling(False),
            PhDos.get_seperator(heading="Batch Execution Done"),
            PhDos.echo_on(),
        ]
        batch_file_path = os.sep.join([PhDos.BATCH_RUN_TC])
        with open(batch_file_path, mode='w') as my_file:
            content = PhUtil.normalise_list(executable_script)
            my_file.write('\n'.join(content))
        PhProcess.run_batch_file(batch_file_path)

    @classmethod
    def tc_is_not_whitelisted(cls, key):
        if TestAutoBatch.white_listed_tcs is None or len(TestAutoBatch.white_listed_tcs) == 0:
            return False
        key_name = PhExecutionModes.get_key_name(key)
        if key_name in TestAutoBatch.white_listed_tcs:
            return False
        return True

    @classmethod
    def test(cls, test_case_data, default_batch_data=None, cli=False):
        """

        :param test_case_data:
        :return:
        """
        PhUtil.print_heading(test_case_data.get(PhKeys.TEST_CASE_ID))
        PhUtil.print_iter(test_case_data, header='test_case_data')
        PhUtil.print_heading('update_variables_in_file', heading_level=2)
        original_data = cls._update_variables_in_file(test_case_data)
        batch_params = test_case_data.get(PhKeys.BATCH_PARAMS) if cli else None
        cls.prepare_batch_file(test_case_data, default_batch_data, batch_params)
        PhUtil.print_heading('clean_up', heading_level=2)
        cls.clean_up(original_data)

    @classmethod
    def test_all(cls):
        """

        :return:
        """

        def _get_test_data(key, dict_data, cli=False):
            key_name = ('cli_' + key) if cli else PhExecutionModes.get_key_name(key)
            dynamic_data = dict_data.get(key, PhConstants.DICT_EMPTY)
            for temp_key in TestData.default_data:
                if temp_key not in dynamic_data:
                    dynamic_data[temp_key] = TestData.default_data[temp_key]
            static_data = {
                PhKeys.TEST_CASE_ID: key_name,
                PhKeys.TEST_CASE_NAME: key_name,
                PhKeys.TEST_CASE_FILE_NAME: f'{key_name}.log'
            }
            return PhUtil.dict_merge(static_data, dynamic_data)

        def _test(dict_data, cli=False):
            for index, key in enumerate(dict_data.keys()):
                if cls.tc_is_not_whitelisted(key):
                    continue
                test_case_data = _get_test_data(key=key, dict_data=dict_data, cli=cli)
                common_data = PhUtil.to_list(PhDos.echo(f'Iteration {index + 1}', wrap_up=True))
                common_data.extend(PhDos.common_info())
                cls.test(test_case_data=test_case_data, default_batch_data=common_data, cli=cli)
            return

        print_configurations()
        if TestAutoBatch.white_listed_tcs is not None:
            TestAutoBatch.white_listed_tcs = [PhExecutionModes.get_key_name(x) for x in TestAutoBatch.white_listed_tcs]
        """
        Non CLI Tests
        """
        _test(TestData.dynamic_data)
        """
        CLI Tests
        """
        TestData.generate_dynamic_cli_from_read_me()
        _test(TestData.dynamic_data_cli, cli=True)


def main():
    """

    :return:
    """
    TestAutoBatch.white_listed_tcs = [
        # PhExecutionModes.ALL,
        # PhExecutionModes.UNIT_TESTING,
    ]
    TestAutoBatch.test_all()


if __name__ == '__main__':
    main()
