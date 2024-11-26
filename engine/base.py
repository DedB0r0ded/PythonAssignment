from random import randint


# ==============__ID_GENERATION__=============
def list_includes_range(lst: list, rng: range):
  lst_set = set(lst)
  rng_set = set(rng)
  return rng_set.issubset(lst_set)


# ==============__ID_GENERATION__=============
def id_validate_int_constraints(min, max, existent_ids):
  if max < min:
    raise ValueError("\'min\' can't be more than \'max\'")
  if min < 0:
    raise ValueError("\'min\' must be greater than or equal to zero.")
  if list_includes_range(existent_ids, range(min, max)):
    raise ValueError("\'existent_ids\' includes the whole [\'min\', \'max\'] range.")


def id_generate_int_unsafe(min, max, existent_ids) -> int:
  id = randint(min, max)
  for i in existent_ids:
    if id == i:
      return id_generate_int_unsafe(min, max, existent_ids)
  return id


# TODO: rename this function. Safe version of id_generate_int(...)
def id_generate_int(min=0, max=100_000_000, existent_ids: list | None = None):
  id_validate_int_constraints(min, max, existent_ids)
  if existent_ids is None or len(existent_ids) == 0:
    return randint(min, max)
  return id_generate_int_unsafe(min, max, existent_ids)


# ==============__CALLABLES__=============
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
