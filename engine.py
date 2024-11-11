# ==============_GENERAL_=============
def build_callable(function_meta: list):
  """Makes a function from [definition, arguments] list"""
  return lambda fun = function_meta[0], args = function_meta[1]: fun(*args)

def callables_flatten(callable_2d_list: list[list]):
  """Makes functions from [[definition, arguments], [...,...], ...] 2D list"""
  return [build_callable(row) for row in callable_2d_list]

def callables(callable_list: list) -> bool:
  """Checks if all list elements are callables (functions/methods)."""
  if not all(callable(f) for f in callable_list):
    return False
  return True

def callables_2d(callable_2d_list: list[list]) -> bool:
  return callables(callables_flatten(callable_2d_list))


# ==============____APP____=============
def app_run(start_callback: callable, exit_callback: callable, menu_functions: list, app_state: dict):
  """
  Runs an application.
  :param start_callback: function called before running the application.
  :param exit_callback: function called before shutting down the application.
  :param menu_functions: functions to call menu and functions called by user choice in menu (with list of arguments).
  :param app_state: initial state of the application
  """
  while app_state["IS_RUNNING"]:
    try:
      if not callable(exit_callback):
        raise TypeError(ERR_PARAM_NOT_CALLABLE)
      if not callable(start_callback):
        raise TypeError(ERR_PARAM_NOT_CALLABLE)
      if not callables_2d(menu_functions):
        raise TypeError(ERR_MENU_ELEM_NOT_CALLABLE)

      try:
        clui_call_menu_start(menu_functions)
        app_state["EXIT_CODE"] = 0
        app_exit(exit_callback, app_state)
      except TypeError as e:
        print("Type error: " + str(e))
      except ValueError as e:
        print("Value error: " + str(e))

    except TypeError as e:
      print("Type error: " + str(e))
      app_state["EXIT_CODE"] = 2001
      app_exit(exit_callback, app_state)
    except ValueError as e:
      print("Value error: " + str(e))
      app_state["EXIT_CODE"] = 2002
      app_exit(exit_callback, app_state)


def app_exit(exit_callback: callable, app_state: dict):
  """Finishes an application.
  :param app_state: application state on the end of execution
  :param exit_callback: function called before shutting down the application."""
  app_state["IS_RUNNING"] = False
  exit_callback()
  print(MSG_EXIT)
  if app_state["DEBUG"]:
    print("Exit code: " + str(app_state["EXIT_CODE"]))


# ==============____CLUI____==============
#Command line user interface
def clui_call_menu_start(functions: list):
  while True:
    option: int = int(input(MENU_START))
    if option == 0:
      return
    if option in range(1, len(functions) + 1):
      build_callable(functions[option - 1])()
    else: raise ValueError(ERR_INVALID_OPTION)

def clui_call_menu_login(functions: list):
  while True:
    option: int = int(input(MENU_LOGIN))
    if option == 0:
      return
    if option in range(1, len(functions) + 1):
      build_callable(functions[option - 1])()
    else: raise ValueError(ERR_INVALID_OPTION)

def clui_print_state(app_state: dict):
  for key, value in app_state.items():
    print(str(key) + ": " + str(value))
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

def str_add_extension_txt(filename: str) -> str:
  """Adds '.txt' to the end of the file name."""
  return filename + ".txt"


# =============____FILES____=============
def file_create(filename: str) -> bool:
  """
  Creates an empty text file if it doesn't exist.
  :param filename:
  :return: True if file was created successfully, else False
  """
  try:
    with open(str_add_extension_txt(filename), 'r') as f:
      return False
  except FileNotFoundError:
    with open(str_add_extension_txt(filename), 'w') as f:
      return True

def file_read_str(filename: str) -> str:
  """
  Reads the whole file as one string if file exists.
  :param filename: string. File name without extension.
  :return: string. File contents as a string.
  """
  try:
    with open(str_add_extension_txt(filename), 'r') as f:
      return f.read()
  except FileNotFoundError:
    print('File not found. Please check the file path.')

def file_read_lines(filename: str) -> list:
  """
  Reads the file line by line if file exists.
  :param filename: string. File name without extension.
  :return: list of strings. File contents as a list of lines.
  """
  try:
    with open(str_add_extension_txt(filename), 'r') as f:
      return [line.strip() for line in f.readlines()]
  except FileNotFoundError:
    print('File not found. Please check the file path.')

def file_write_str(filename: str, content: str) -> bool:
  """
  Adds a string to the end of the file. Creates a new file if it doesn't exist.
  :param filename: string. File name without extension.
  :param content: string to be appended to the end of the file.
  :return: True if string was written successfully, else False.
  """
  with open(str_add_extension_txt(filename), 'a') as f:
    f.write(content)
    return True


def file_write_line(filename: str, content: str) -> bool:
  """
  Adds a string and a new line to the end of the file. Creates a new file if it doesn't exist.
  :param filename: string. File name without extension.
  :param content: string to be appended to the end of the file.
  :return: True if string was written successfully, else False.
  """
  return file_write_str(filename, content + "\n")