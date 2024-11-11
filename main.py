import engine
import administrator as admin
import doctor
import nurse
import patient
import receptionist as rcpst


# ================_STATE_===============
state = {"IS_RUNNING": True, "DEBUG": True}

# ==============_FUNCTIONS_=============
def on_start():
  pass

def on_exit():
  pass

functions = [
  [engine.clui_call_menu_login, [
    [
      [lambda: print("`Administrator interface`. Empty for now. Returning to log in menu..."), []],
      [lambda: print("`Doctor interface`. Empty for now. Returning to log in menu..."), []],
      [lambda: print("`Nurse interface`. Empty for now. Returning to log in menu..."), []],
      [lambda: print("`Patient interface`. Empty for now. Returning to log in menu..."), []],
      [lambda: print("`Receptionist interface`. Empty for now. Returning to log in menu..."), []],
    ]]
   ],
  [engine.clui_print_state,
    [state]
  ]
]


# =============ENTRY_POINT==============
if __name__ == '__main__':
  engine.app_run(on_start, on_exit, functions, state)