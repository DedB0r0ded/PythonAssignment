from .base import *


# ==============____CLUI____==============
#Command line user interface
def clui_call_menu(functions: list, menu_str: str):
  while True:
    option: int = int(input(menu_str))
    if option == 0:
      return
    if option in range(1, len(functions) + 1):
      build_callable(functions[option - 1])()
    else:
      raise ValueError(ERR_INVALID_OPTION)


def clui_call_menu_start(functions: list):
  clui_call_menu(functions, MENU_START)


def clui_call_menu_login(functions: list):
  clui_call_menu(functions, MENU_LOGIN)


def clui_print_state(app_state: dict):
  for key, value in app_state.items():
    print(str(key) + ": " + str(value))
