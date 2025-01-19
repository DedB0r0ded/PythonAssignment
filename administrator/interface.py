import datetime

from engine import APPLICATION_STATE, app_set_param, app_enforce_file_check, app_debug, app_start_callback, \
  app_exit_callback
from .resources import *
from .users import *


MAIN_MENU: str = """
=================
1. Manage accounts
2. View hospital statistics
3. Generate report on hospital usage and occupancy rates
4. Manage hospital resources
5. Set operational rules and policies
0. Back
=================
"""

USER_CREATE_MENU: str = """
=================
Select user role:
1. Administrator
2. Doctor
3. Nurse
4. Patient
5. Receptionist
0. Exit user creation
=================
"""

ACCOUNT_MENU: str = """
=================
1. Create an account
2. Update an existing account
3. Delete an existing account
0. Back
=================
"""

RESOURCES_MENU: str = """
=================
1. Add a bed
2. Remove a bed
3. Add facility
4. Remove facility
0. Back
=================
"""

RULES_MENU: str = """
=================
1. Switch ENFORCE_FILE_CHECK - if True, ensures that all the necessary files exist before the application starts.
2. Switch DEBUG_MODE - if True, shows ERROR_CODE and EXIT_CODE when application finished.
3. Switch START_CALLBACK - if True, calls on_start() function when application is started.
4. Switch EXIT_CALLBACK - if True, calls on_exit() function when application is finished.
0. Back
=================
"""


def call_user_create_menu():
  user = {}
  user["email"] = input("Enter user email: ").strip()
  user["password"] = input("Enter user password: ").strip()
  while True:
    print(USER_CREATE_MENU)
    choice: str = input("Enter your choice: ").strip()
    if choice == "1":
      user["role"] = "admin"
      break
    elif choice == "2":
      user["role"] = "doctor"
      break
    elif choice == "3":
      user["role"] = "nurse"
      break
    elif choice == "4":
      user["role"] = "patient"
      break
    elif choice == "5":
      user["role"] = "receptionist"
      break
    elif choice == "0":
      print("Leaving the menu...")
      return
    else:
      print("Invalid choice. Try again.")
  user["registration_date"] = datetime.date.today()
  return user


def call_user_new_menu():
  print("Starting user creation...")
  user = call_user_create_menu()
  if not user:
    print("User creation failed.")
  else:
    user_create(user)
    print("User created successfully.")


def call_user_update_menu() -> dict | None:
  print("Starting user update...")
  user = {}
  user["id"] = int(input("Enter user id: ").strip())
  user_temp = call_user_create_menu()
  if not user_temp:
    print("User update failed.")
  else:
    user.update(user_temp)
    if user_update(user):
      print("User updated successfully.")
    else:
      print("User update failed.")


def call_user_delete_menu():
  print("Starting user delete...")
  user_id = input("Enter user id: ").strip()
  if user_delete(user_id):
    print("User deleted successfully.")
  else:
    print("User deletion failed.")


def call_user_menu():
  while True:
    print(ACCOUNT_MENU)
    choice: str = input("Enter your choice: ").strip()
    if choice == "1":
      call_user_new_menu()
    elif choice == "2":
      call_user_delete_menu()
    elif choice == "3":
      print("Starting user deletion...")
      call_user_delete_menu()
    elif choice == "0":
      print("Leaving user managing menu...")
      break
    else:
      print("Invalid choice. Try again.")


def show_statistics():
  beds_total = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]["beds"]
  beds_used = 0
  beds_free = beds_total - beds_used

  facility_total = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]["facility"]

  patients_all = e.csv_read(e.FILE_NAMES["PATIENTS"])
  patients_current = []
  for p in patients_all:
    if p["status"] == "hospitalized":
      patients_current.append(p)

  beds_used = patients_total = len(patients_current)

  doctors_total = len(e.csv_read(e.FILE_NAMES["DOCTORS"]))

  print("\nHospital statistics")
  print(f"Total number of patients: {patients_total}")
  print(f"Beds available: {beds_total - beds_used}/{beds_total}")
  print(f"Total number of doctors working: {doctors_total}")
  print(f"Total facility number: {facility_total}")


def show_report():
  beds_total = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]["beds"]
  patients_all = e.csv_read(e.FILE_NAMES["PATIENTS"])
  patients_current = []
  for p in patients_all:
    if p["status"] == "hospitalized":
      patients_current.append(p)
  print("=================")
  print("Overall hospitalization report")
  print(f"Total patients: {len(patients_all)}")
  print(f"Currently hospitalized patients: {len(patients_current)}")
  print(f"Patients discharged: {len(patients_all) - len(patients_current)}")
  print(f"Occupancy rate: {len(patients_current)/beds_total}%")
  print("=================")


def call_resources_menu():
  init_resource_file()
  while True:
    print(RESOURCES_MENU)
    choice: str = input("Enter your choice: ").strip()
    if choice == "1":
      resources_add_bed()
      print("Bed was added.")
    elif choice == "2":
      resources_remove_bed()
      print("Bed was removed.")
    elif choice == "3":
      resources_add_facility()
      print("Facility was added.")
    elif choice == "4":
      resources_remove_facility()
      print("Facility was removed.")
    elif choice == "0":
      print("Leaving this menu...")
      break
    else:
      print("Invalid choice. Try again.")


def call_param_switch_menu(param_name: str, new_value):
  print(f"Are you sure you want to set {param_name} to {new_value}? (y/n)")
  choice: str = input("").strip()
  if choice == "y":
    app_set_param(param_name, new_value)
    e.csv_rewrite(e.FILE_NAMES["APP_STATE"], [APPLICATION_STATE])
    print("Value changed successfully. Returning to the previous menu...")
  elif choice == "n":
    print("Operation cancelled. Returning to the previous menu...")
  else:
    print("Invalid choice. Try again.")
    call_param_switch_menu(param_name, new_value)


def call_rules_menu():
  while True:
    print(RULES_MENU)
    choice: str = input("Enter your choice: ").strip()
    if choice == "1":
      call_param_switch_menu("ENFORCE_FILE_CHECK", not app_enforce_file_check())
    elif choice == "2":
      call_param_switch_menu("DEBUG_MODE", not app_debug())
    elif choice == "3":
      call_param_switch_menu("START_CALLBACK", not app_start_callback())
    elif choice == "4":
      call_param_switch_menu("EXIT_CALLBACK", not app_exit_callback())
    elif choice == "0":
      print("Leaving this menu...")
      break
    else:
      print("Invalid choice. Try again.")


def call_main_menu():
  while True:
    print(MAIN_MENU)
    choice: str = input("Enter your choice: ").strip()
    if choice == "1":
      call_user_menu()
    elif choice == "2":
      show_statistics()
    elif choice == "3":
      show_report()
    elif choice == "4":
      call_resources_menu()
    elif choice == "5":
      call_rules_menu()
    elif choice == "0":
      print("Leaving admin menu...")
      break
    else:
      print("Invalid choice. Try again.")
