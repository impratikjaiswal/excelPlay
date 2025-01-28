import os

from python_helpers.ph_constants import PhConstants

from excel_play.main.data_type.data_type_master import DataTypeMaster
from excel_play.main.helper.data import Data
from excel_play.main.helper.folders import Folders
from excel_play.main.helper.formats import Formats


class UnitTesting(DataTypeMaster):

    def __init__(self):
        super().__init__()

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_data_pool(self):
        input_items_list_w_output_folder = [
            Folders.in_sample('Excel Worksheet1.xlsx'),
            Folders.in_sample(),
            r'D:\Other\Github_Self\excelPlay\data\sample_data\Excel Worksheet1.xlsx',
            r'D:\Other\Github_Self\excelPlay\data\sample_data',
            r'D:\\Other\\Github_Self\\excelPlay\\data\\sample_data\\Excel Worksheet1.xlsx',
            r'D:/Other/Github_Self/excelPlay/data/sample_data/Excel Worksheet1.xlsx',
        ]

        input_items_list_wo_output_folder = [
            Folders.in_test_logs('TC_wo_out_folder_0'),
            Folders.in_test_logs('TC_wo_out_folder_1'),
            Folders.in_test_logs(['TC_wo_out_folder_2', 'Excel Worksheet2.xlsx']),
        ]

        input_items_list_zip = [
            Folders.in_test_logs('TC_zip_0'),
            Folders.in_test_logs('TC_zip_1'),
            Folders.in_test_logs(['TC_zip_2', 'SampleData 3.0.6.56.xlsx']),
        ]

        input_items_list_encoding_ascii = [
            Folders.in_test_logs('TC_encoding_ascii_0'),
        ]

        data_pool_input_items_list_w_output_folder = []
        remarks = 'input_items_list_w_output_folder'
        for index, input_item in enumerate(input_items_list_w_output_folder):
            output_path = Folders.in_test_logs(f'TC_{index}')
            data = Data(input_data=input_item, output_path=output_path, remarks=remarks, archive_output=False)
            data_pool_input_items_list_w_output_folder.append(data)
        #
        data_pool_input_items_list_wo_output_folder = []
        remarks = 'input_items_list_wo_output_folder'
        for index, input_item in enumerate(input_items_list_wo_output_folder):
            data = Data(input_data=input_item, remarks=remarks, archive_output=False)
            data_pool_input_items_list_wo_output_folder.append(data)
        #
        data_pool_input_items_list_zip = []
        remarks = 'input_items_list_zip'
        for index, input_item in enumerate(input_items_list_zip):
            data = Data(input_data=input_item, output_archive_format=Formats.ZIP, remarks=remarks)
            data_pool_input_items_list_zip.append(data)
        #
        data_pool_input_items_list_multi = []
        remarks = 'input_items_list_multi'
        data = Data(input_data=input_items_list_w_output_folder, output_archive_format=Formats.ZIP, remarks=remarks)
        data_pool_input_items_list_multi.append(data)
        #
        data_pool_input_items_tuple_multi = []
        remarks = 'input_items_tuple_multi'
        data = Data(input_data=tuple(input_items_list_w_output_folder), output_archive_format=Formats.ZIP,
                    remarks=remarks)
        data_pool_input_items_tuple_multi.append(data)
        #
        data_pool_input_items_list_multi_w_output_folder = []
        remarks = 'input_items_list_multi_w_output_folder'
        output_path = Folders.in_test_logs(f'TC_input_items_list_multi_w_output_folder')
        data = Data(input_data=input_items_list_w_output_folder, output_archive_format=Formats.ZIP, remarks=remarks,
                    output_path=output_path
                    )
        data_pool_input_items_list_multi_w_output_folder.append(data)
        #
        data_pool_input_items_tuple_multi_w_output_folder = []
        remarks = 'input_items_tuple_multi_w_output_folder'
        output_path = Folders.in_test_logs(f'TC_input_items_tuple_multi_w_output_folder')
        data = Data(input_data=tuple(input_items_list_w_output_folder), output_archive_format=Formats.ZIP,
                    remarks=remarks, output_path=output_path
                    )
        data_pool_input_items_tuple_multi_w_output_folder.append(data)
        #
        data_pool_input_items_list_encoding = []
        remarks = 'input_items_list_encoding'
        for index, input_item in enumerate(input_items_list_encoding_ascii):
            for encoding_errors in PhConstants.CHAR_ENCODING_ERRORS_POOL:
                output_path = os.sep.join([input_item, encoding_errors])
                data = Data(input_data=input_item, archive_output=False, output_path=output_path,
                            remarks=remarks, encoding=PhConstants.CHAR_ENCODING_ASCII, encoding_errors=encoding_errors)
                data_pool_input_items_list_encoding.append(data)
        #
        data_pool_positive = [
            #
        ]
        data_pool_negative = [
            #  without any parameters
            Data(),
            #
            Data(input_data='xyz', remarks='invalid path')
            #
        ]
        #
        super().set_data_pool(
            data_pool_positive

            + data_pool_input_items_list_w_output_folder
            + data_pool_input_items_list_wo_output_folder
            + data_pool_input_items_list_zip
            + data_pool_input_items_list_multi
            + data_pool_input_items_tuple_multi
            + data_pool_input_items_list_multi_w_output_folder
            + data_pool_input_items_tuple_multi_w_output_folder
            + data_pool_input_items_list_encoding
            + data_pool_negative
        )
