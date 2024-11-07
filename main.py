import utils
import administrator as admin
import doctor
import nurse
import patient
import receptionist as rcpst


#================_STATE_===============
state = {"IS_RUNNING": True}

#==============_FUNCTIONS_=============
def on_start():
	pass

def on_exit():
	pass

lambdas = [
	lambda: print("`Administrator interface`. Empty for now. Returning to log in menu..."),
	lambda: print("`Doctor interface`. Empty for now. Returning to log in menu..."),
	lambda: print("`Nurse interface`. Empty for now. Returning to log in menu..."),
	lambda: print("`Patient interface`. Empty for now. Returning to log in menu..."),
	lambda: print("`Receptionist interface`. Empty for now. Returning to log in menu..."),
]


#=============ENTRY_POINT==============
if __name__ == '__main__':
	utils.app_run(on_start, on_exit, lambdas, state)