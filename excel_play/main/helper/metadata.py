from collections import OrderedDict

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil


class MetaData:
    def __init__(self, input_data_org):
        # Common Param
        self.transaction_id = PhUtil.generate_transaction_id()
        self.input_data_org = input_data_org
        self.parsed_data = None
        self.operation_mode = None
        self.input_mode_key = None
        self.output_file_path = None
        self.include_files = None
        self.excludes = None
        self.output_dic = OrderedDict()
        self.input_mode_value = str(self.input_data_org)
        #
        self.output_file_ext_default = None
        self.output_file_location_default = None

    def get_info_data(self):
        if self.output_dic:
            info = self.output_dic.get(PhKeys.INFO, None)
            if info is not None:
                return str(info)
        return PhConstants.STR_EMPTY

    def get_parsed_data(self):
        return self.parsed_data
