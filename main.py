import engine
import administrator as admin
import doctor
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
      [lambda: admin.call_main_menu(), []],

      [lambda: doctor.main(), []],

      [lambda: nurse.main(), []],

      [lambda: patient.main(), []],

      [lambda: receptionist.receptionist_menu(), []],
    ]]
   ],
  [engine.clui_print_state,
    []
  ]
]


# =============ENTRY_POINT==============
if __name__ == '__main__':
  engine.application.app_run(on_start, on_exit, functions)
