from excel_play.main.data_type.data_type_master import DataTypeMaster
from excel_play.main.helper.data import Data


class UserData(DataTypeMaster):

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

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_output_format(self):
        output_format = None
        super().set_output_format(output_format)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='Sample Excel Worksheet1.xlsx',
                input_data=r'D:\Other\Github_Self\excelPlay\data\sampleData\SampleData.xlsx',
            ),
        ]
        super().set_data_pool(data_pool)
