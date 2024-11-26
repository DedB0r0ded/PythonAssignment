from .interface import *


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
  if app_state["DEBUG_MODE"]:
    print("Exit code: " + str(app_state["EXIT_CODE"]))