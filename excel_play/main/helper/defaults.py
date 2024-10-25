from python_helpers.ph_constants import PhConstants

from excel_play.main.helper.formats import Formats


class Defaults:
    DEFAULT_FORMAT = Formats.CSV
    DEFAULT_ARCHIVE_FORMAT = Formats.ZIP
    DEFAULT_ENCODING_FORMAT = PhConstants.STR_ENCODING_FORMAT_UTF8
    DEFAULT_ENCODING_ERROR_HANDLING = PhConstants.STR_ENCODING_ERROR_HANDLING_IGNORE
