import engine as e


# User CRUD
def user_create(user: dict = None):
  e.csv_write_user(user)


def user_read(id: str) -> dict:
  accounts = e.csv_read(e.FILE_NAMES["USERS"])
  for account in accounts:
    if account["id"] == id:
      return account


def user_update(user: dict = None):
  users = e.csv_read(e.FILE_NAMES["USERS"])
  for a in users:
    if a["id"] == user["id"]:
      a["password"] = user["password"]
      a["email"] = user["email"]
      a["role"] = user["role"]
      a["registration_date"] = user["registration_date"]
      e.csv_rewrite(e.FILE_NAMES["USERS"], users)
      return True
  return False


def user_delete(id: str) -> dict | None:
  users = e.csv_read(e.FILE_NAMES["USERS"])
  users_new = []
  res = {}
  user_exists = False
  for user in users:
    if user["id"] == id:
      user_exists = True
      break
  if not user_exists:
    return None
  for user in users:
    if user["id"] != id:
      users_new.append(user)
      res = user
  e.csv_rewrite(e.FILE_NAMES["USERS"], users_new)
  return res
