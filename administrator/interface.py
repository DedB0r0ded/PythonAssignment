from .resources import *
from .accounts import *

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


def call_main_menu():
  while True:
    print(MAIN_MENU)
    choice: str = input("Enter your choice: ").strip()
    if choice == "1":
      call_account_menu()
    elif choice == "2":
      show_statistics()
    elif choice == "3":
      pass
    elif choice == "4":
      pass
    elif choice == "5":
      pass
    elif choice == "0":
      print("Leaving admin menu...")
      break
    else:
      print("Invalid choice. Try again.")


def call_account_menu():
  print(ACCOUNT_MENU)


def show_statistics():
  beds_total = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]["beds"]
  beds_used = 0
  beds_free = beds_total - beds_used

  facility_total = e.csv_read(e.FILE_NAMES["RESOURCES"])[0]["facilities"]

  patients_total = len(e.csv_read(e.FILE_NAMES["PATIENTS"]))

  doctors_total = len(e.csv_read(e.FILE_NAMES["DOCTORS"]))

  print("\nHospital statistics")
  print(f"Total beds: {beds_total}")
  print(f"Beds used: {2}; Free beds: {beds_total - 2}")
  print(f"Total facility quantity: {e.csv_read(e.FILE_NAMES["RESOURCES"])[0]["facility"]}")


def show_report():
  pass


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