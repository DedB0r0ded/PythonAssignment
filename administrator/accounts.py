import engine as e


# Account CRUD
def account_create(account: dict = None):
  e.csv_write_entity(e.FILE_NAMES["ACCOUNTS"], account)


def account_read(id: str) -> dict:
  accounts = e.csv_read(e.FILE_NAMES["ACCOUNTS"])
  for account in accounts:
    if account["id"] == id:
      return account


def account_update(account: dict = None):
  accounts = e.csv_read(e.FILE_NAMES["ACCOUNTS"])
  for a in accounts:
    if a["id"] == account["id"]:
      a["password"] = account["password"]
      a["name"] = account["name"]
      a["email"] = account["email"]
      a["role"] = account["role"]
  e.csv_rewrite(e.FILE_NAMES["ACCOUNTS"], accounts)


def account_delete(id: str) -> dict:
  accounts = e.csv_read(e.FILE_NAMES["ACCOUNTS"])
  accounts_new = []
  res = {}
  for account in accounts:
    if account["id"] != id:
      accounts_new.append(account)
      res = account
  e.csv_rewrite(e.FILE_NAMES["ACCOUNTS"], accounts_new)
  return res