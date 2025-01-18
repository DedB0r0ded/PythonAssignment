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
  "ENFORCE_FILE_CHECK": None,
  "ALL_FILES_EXIST": None,
  "ERROR_CODE": 0,
  "EXIT_CODE": 0
}


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


# ==============_FILE_NAMES_===============
FILE_NAMES = {
  "APPOINTMENTS":           "./files/appointments.txt",
  "BILLING":                "./files/billing.txt",
  "CHECK_IN":               "./files/check_in.txt",
  "CHECK_OUT":              "./files/check_out.txt",

  "ACCOUNTS":               "./files/accounts.csv",
  "RESOURCES":              ",/files/resources.csv",
  
  "PATIENTS_RECEPTIONIST":  "./files/patients.txt",

  "PATIENTS_DOCTOR":        "./files/patient_data.txt",
  "DOCTORS":                "./files/doctor_data.txt",

  "PATIENTS":               "./files/patients.csv",
  "VITALS":                 "./files/vitals.csv",
  "MEDICATION_LOGS":        "./files/medication_logs.csv",
  "ROOM_PREP":              "./files/room_prep.csv",
}


# ============____STRINGS____============
MENU_START: str = """
==========
1. Log in
2. Application info
0. Exit
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
