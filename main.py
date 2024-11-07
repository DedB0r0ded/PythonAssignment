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
	lambda: print("`Administrator interface`"),
	lambda: print("`Doctor interface`"),
	lambda: print("`Nurse interface`"),
	lambda: print("`Patient interface`"),
	lambda: print("`Receptionist interface`"),
]


#=============ENTRY_POINT==============
if __name__ == '__main__':
	utils.app_run(on_start, on_exit, lambdas, state)