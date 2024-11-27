# ==============____ERROR_CODES____=============
EXCEPTION_TYPE_OFFSET = 24
ERROR_TYPE_OFFSET = 8
ERROR_NAME_OFFSET = 0

TYPE_ERROR = 0 << EXCEPTION_TYPE_OFFSET
VALUE_ERROR = 1 << EXCEPTION_TYPE_OFFSET

#TODO: add all possible errors here
ID_VALIDATION_ERROR = VALUE_ERROR + 1 << ERROR_TYPE_OFFSET


# ==============_APPLICATION_STATE_=============
APPLICATION_STATE = {
  "IS_RUNNING": True,
  "DEBUG_MODE": True,
  "ERROR_CODE": 0,
  "EXIT_CODE": 0
}


def app_set_is_running(is_running: bool):
  APPLICATION_STATE['IS_RUNNING'] = is_running


def app_set_debug(debug: bool):
  APPLICATION_STATE['DEBUG'] = debug


def app_set_error_code(error_code: int):
  APPLICATION_STATE['ERROR_CODE'] = error_code


def app_set_exit_code(exit_code: int):
  APPLICATION_STATE['EXIT_CODE'] = exit_code


def app_is_running():
  return APPLICATION_STATE['IS_RUNNING']


def app_debug():
  return APPLICATION_STATE['DEBUG_MODE']


def app_error_code():
  return APPLICATION_STATE['ERROR_CODE']


def app_exit_code():
  return APPLICATION_STATE['EXIT_CODE']