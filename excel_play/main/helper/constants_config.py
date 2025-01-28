from excel_play._git_info import GIT_SUMMARY
from excel_play._tool_name import TOOL_NAME
from excel_play._version import __version__


class ConfigConst:
    TOOL_VERSION = __version__.public()
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = 'Excel Play'
    TOOL_GIT_SUMMARY = GIT_SUMMARY
    TOOL_DESCRIPTION = f'Split Microsoft Excel file to individual CSV file(s) containing one sheet per file. Multiple input files can be fed in one shot.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION}'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, Excel CSV Export, excel, microsoft excel, excel export,excel export csv, xlsx, xls, csv, comma seperated values'
    TOOL_URL = 'https://github.com/impratikjaiswal/excelPlay'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/excelPlay/issues'
