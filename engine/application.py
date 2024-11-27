from .interface import *


# ==============APPLICATION_LOGIC=============
def app_run(start_callback: callable, exit_callback: callable, menu_functions: list):
  """
  Runs an application.
  :param start_callback: function called before running the application.
  :param exit_callback: function called before shutting down the application.
  :param menu_functions: functions to call menu and functions called by user choice in menu (with list of arguments).
  """
  while app_is_running():
    try:
      if not callable(exit_callback):
        raise TypeError(ERR_PARAM_NOT_CALLABLE)
      if not callable(start_callback):
        raise TypeError(ERR_PARAM_NOT_CALLABLE)
      if not callables_2d(menu_functions):
        raise TypeError(ERR_MENU_ELEM_NOT_CALLABLE)

      try:
        clui_call_menu_start(menu_functions)
        app_set_exit_code(0)
        app_exit(exit_callback)
      except TypeError as e:
        print("Type error: " + str(e))
      except ValueError as e:
        print("Value error: " + str(e))

    except TypeError as e:
      print("Type error: " + str(e))
      app_set_exit_code(TYPE_ERROR)
      app_exit(exit_callback)
    except ValueError as e:
      print("Value error: " + str(e))
      app_set_exit_code(VALUE_ERROR)
      app_exit(exit_callback)


def app_exit(exit_callback: callable):
  """Finishes an application.
  :param exit_callback: function called before shutting down the application."""
  app_set_is_running(False)
  exit_callback()
  print(MSG_EXIT)
  if app_debug():
    print("Exit code: " + str(app_exit_code()))