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


# ==============_FILE_NAMES_===============
FILE_NAMES = {
  "APP_STATE":              "./files/app_state.csv",

  "IDS":                    "./files/ids.csv",
  "SERVICES":               "./files/services.csv",
  "BILLING":                "./files/billing.csv",
  "USERS":                  "./files/users.csv",
  "RESOURCES":              "./files/resources.csv",
  "DOCTORS":                "./files/doctors.csv",
  "PATIENTS":               "./files/patients.csv",
  "MEDICATION_LOGS":        "./files/medication_logs.csv",
  "MEDICAL_HISTORY":        "./files/medical_history.csv",
  "ROOM_PREP":              "./files/room_prep.csv",
}
DEEP_FILE_NAMES = dict(zip(FILE_NAMES.keys(), ['.' + v for v in FILE_NAMES.values()]))


# ==============_APPLICATION_STATE_=============
APPLICATION_STATE = {
  "IS_RUNNING": False,
  "DEBUG_MODE": False,
  "ENFORCE_FILE_CHECK": False,
  "ALL_FILES_EXIST": False,
  "START_CALLBACK": False,
  "EXIT_CALLBACK": False,
  "ERROR_CODE": 0,
  "EXIT_CODE": 0
}


def __file_read_lines(filename: str) -> list:
  try:
    with open(filename, 'r') as f:
      return [line.strip() for line in f.readlines()]
  except FileNotFoundError:
    print(f'File \"{filename}\" not found. Please check the file path.')


def __csv_read(filename: str) -> list:
  lines = __file_read_lines(filename)
  header_lst = map(str.strip, lines.pop(0).strip().split(','))
  result = []
  for line in lines:
    line_lst = map(str.strip, line.strip().split(','))
    result.append(dict(zip(header_lst, line_lst )))
  return result


def app_refresh_app_state():
  with open(FILE_NAMES["APP_STATE"], "r") as f:
    f.readlines()
  state_file = __csv_read(FILE_NAMES["APP_STATE"])[0]
  for k in state_file.keys():
    if state_file[k] == 'True':
      APPLICATION_STATE[k] = True
    elif state_file[k] == 'False':
      APPLICATION_STATE[k] = False
    else:
      APPLICATION_STATE[k] = int(state_file[k])


def app_set_param(param_name: str, param_value: int | bool):
  APPLICATION_STATE[param_name] = param_value


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


def app_enforce_file_check():
  return APPLICATION_STATE['ENFORCE_FILE_CHECK']


def app_start_callback():
  return APPLICATION_STATE['START_CALLBACK']


def app_exit_callback():
  return APPLICATION_STATE['EXIT_CALLBACK']


# ============____STRINGS____============
MENU_START: str = """
==========
1. Log in
0. Quit
==========
"""

MENU_LOGIN: str = """
=================
1. Administrator
2. Doctor
3. Nurse
4. Patient
5. Receptionist
0. Back
=================
"""

ERR_INVALID_OPTION: str = "Invalid option. Try again."
ERR_PARAM_NOT_CALLABLE: str = "One or many callback parameters of app_run function are not callables"
ERR_MENU_ELEM_NOT_CALLABLE: str = "All list elements must be callables."

MSG_EXIT: str = "Application is shutting down..."

EXT_CSV: str = "csv"
