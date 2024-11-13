import engine

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


def call_main_menu(functions: list):
  engine.clui_call_menu(functions, MAIN_MENU)


def call_account_menu(functions: list):
  engine.clui_call_menu(functions, ACCOUNT_MENU)
