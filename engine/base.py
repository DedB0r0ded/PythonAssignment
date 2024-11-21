# ==============__GENERAL__=============
def build_callable(function_meta: list):
  """Makes a function from [definition, arguments] list"""
  return lambda fun=function_meta[0], args=function_meta[1]: fun(*args)


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
