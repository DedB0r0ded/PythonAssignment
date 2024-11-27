import engine
import administrator as admin
#import doctor
import nurse
import patient
import receptionist


# ==============_FUNCTIONS_=============
def on_start():
  pass


def on_exit():
  pass


def plc():
  """Empty placeholder function"""
  pass

plcs = [plc, []]

functions = [
  [engine.clui_call_menu_login, [
    [
      [admin.call_main_menu,
       [[[admin.call_account_menu, [[plcs, plcs, plcs]]], plcs, plcs, plcs, plcs, ]]
       ],

      [lambda: print("`Doctor interface`. Empty for now. Returning to log in menu..."), []],

      [lambda: print("`Nurse interface`. Empty for now. Returning to log in menu..."), []],

      [lambda: print("`Patient interface`. Empty for now. Returning to log in menu..."), []],

      [lambda: print("`Receptionist interface`. Empty for now. Returning to log in menu..."), []],
    ]]
   ],
  [engine.clui_print_state,
    []
  ]
]


# =============ENTRY_POINT==============
if __name__ == '__main__':
  engine.application.app_run(on_start, on_exit, functions)
