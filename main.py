from datetime import datetime

import engine
import administrator as admin
import doctor
import nurse
import patient
import receptionist


# ==============_FUNCTIONS_=============
def on_start():
  print("on_start function called")


def on_exit():
  print("on_exit function called")


def plc():
  """Empty placeholder function"""
  pass


def login(id, pwd, role: str):
  id = str(id).strip()
  users = engine.csv_read(engine.FILE_NAMES["USERS"])
  for user in users:
    if user["id"] == id and user["role"] == role and user["password"] == pwd:
      return True
  return False


def login_input() -> dict:
  user = {}
  user["id"] = input("Your ID: ").strip()
  user["password"] = input("Your password: ").strip()
  return user


def login_admin():
  user = login_input()
  print("Logging in as admin...")
  if login(user["id"], user["password"], "admin"):
    print("Logged in as admin")
    admin.call_main_menu()
  else:
    print("Login failed. Going back to main menu...")


def login_doctor():
  user = login_input()
  print("Logging in as doctor...")
  if login(user["id"], user["password"], "doctor"):
    print("Logged in as doctor")
    doctor.main()
  else:
    print("Login failed. Going back to main menu...")


def login_nurse():
  user = login_input()
  print("Logging in as nurse...")
  if login(user["id"], user["password"], "nurse"):
    print("Logged in as nurse")
    nurse.main()
  else:
    print("Login failed. Going back to main menu...")


def login_patient():
  user = login_input()
  print("Logging in as patient...")
  if login(user["id"], user["password"], "patient"):
    print("Logged in as patient")
    patient.main()
  else:
    print("Login failed. Going back to main menu...")


def login_receptionist():
  user = login_input()
  print("Logging in as receptionist...")
  if login(user["id"], user["password"], "receptionist"):
    print("Logged in as receptionist")
    receptionist.receptionist_menu()
  else:
    print("Login failed. Going back to main menu...")


plcs = [plc, []]

functions = [
  [engine.clui_call_menu_login, [
    [
      [lambda: login_admin(), []],

      [lambda: login_doctor(), []],

      [lambda: login_nurse(), []],

      [lambda: login_patient(), []],

      [lambda: login_receptionist(), []],
    ]]
   ],
]


# =============ENTRY_POINT==============
if __name__ == '__main__':
  engine.application.app_run(on_start, on_exit, functions)
