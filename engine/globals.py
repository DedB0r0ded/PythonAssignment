# ==============____ERROR_CODES____=============
#
# XXX.XXX.XXX.XXX <-- Error code
#  ^   ^   ^   ^
#  |   |   |   |
#  |   |   Error name (6 digits)
#  |   |
#  |   Error type (3 digits)
#  |
# Exception type (3 digits)

EXCEPTION_TYPE_OFFSET = 10 ** 9
ERROR_TYPE_OFFSET = 10 ** 6
ERROR_NAME_OFFSET = 10 ** 0

TYPE_ERROR = 1 * EXCEPTION_TYPE_OFFSET
VALUE_ERROR = 2 * EXCEPTION_TYPE_OFFSET
FILE_NOT_FOUND_ERROR = 3 * EXCEPTION_TYPE_OFFSET

#TODO: add all possible errors here
ID_VALIDATION_ERROR = VALUE_ERROR + (1 * 10 ** ERROR_TYPE_OFFSET)
UNDEFINED_FILE_NOT_FOUND_ERROR = FILE_NOT_FOUND_ERROR

# ==============_APPLICATION_STATE_=============
APPLICATION_STATE = {
  "IS_RUNNING": True,
  "DEBUG_MODE": True,
  "ALL_FILES_EXIST": None,
  "ERROR_CODE": 0,
  "EXIT_CODE": 0
}


def app_set_is_running(is_running: bool):
  APPLICATION_STATE['IS_RUNNING'] = is_running


def app_set_debug(debug: bool):
  APPLICATION_STATE['DEBUG'] = debug


def app_set_files_exist(files_exist: bool):
  APPLICATION_STATE['ALL_FILES_EXIST'] = files_exist


def app_set_error_code(error_code: int):
  APPLICATION_STATE['ERROR_CODE'] = error_code


def app_set_exit_code(exit_code: int):
  APPLICATION_STATE['EXIT_CODE'] = exit_code


def app_is_running():
  return APPLICATION_STATE['IS_RUNNING']


def app_debug():
  return APPLICATION_STATE['DEBUG_MODE']


def app_files_exist():
  return APPLICATION_STATE['ALL_FILES_EXIST']


def app_error_code():
  return APPLICATION_STATE['ERROR_CODE']


def app_exit_code():
  return APPLICATION_STATE['EXIT_CODE']


# ==============_FILE_NAMES_===============
FILE_NAMES = {
  "PATIENTS_FILE":          "./files/patients.txt",
  "VITALS_FILE":            "./files/vitals.txt",
  "MEDICATION_LOGS_FILE":   "./files/medication_logs.txt",
  "ROOM_PREP_FILE":         "./files/room_prep.txt",
}

PATIENTS_FILE = FILE_NAMES["PATIENTS_FILE"]
VITALS_FILE = FILE_NAMES["VITALS_FILE"]
MEDICATION_LOGS_FILE = FILE_NAMES["MEDICATION_LOGS_FILE"]
ROOM_PREP_FILE = FILE_NAMES["ROOM_PREP_FILE"]