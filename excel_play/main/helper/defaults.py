from python_helpers.ph_defaults import PhDefaults
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

from excel_play.main.helper.formats import Formats


class Defaults:
    PRINT_INFO = PhDefaults.PRINT_INFO
    PRINT_INPUT = PhDefaults.PRINT_INPUT
    PRINT_OUTPUT = PhDefaults.PRINT_OUTPUT
    ARCHIVE_OUTPUT = PhDefaults.ARCHIVE_OUTPUT
    QUITE_MODE = PhDefaults.QUITE_MODE
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    ENCODING = PhDefaults.CHAR_ENCODING
    ENCODING_ERRORS = PhDefaults.ENCODING_ERRORS
    ARCHIVE_OUTPUT_FORMAT = PhDefaults.ARCHIVE_OUTPUT_FORMAT
    #
    OUTPUT_FORMAT = Formats.CSV
    OUTPUT_PATH = None
