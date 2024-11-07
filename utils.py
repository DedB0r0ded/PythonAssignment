#==============_GENERAL_=============
def callables(callable_list: list) -> bool:
	if not all(callable(f) for f in callable_list):
		return False
	return True

#==============____APP____=============
def app_run(start_callback: callable, exit_callback: callable, login_functions: list, app_state: dict):
	while app_state["IS_RUNNING"]:
		try:
			if not callable(exit_callback):
				raise TypeError(ERR_PARAM_NOT_CALLABLE)
			if not callable(start_callback):
				raise TypeError(ERR_PARAM_NOT_CALLABLE)
			if not callables(login_functions):
				raise TypeError(ERR_MENU_ELEM_NOT_CALLABLE)

			if not cli_call_menu_start(start_callback, login_functions):
				app_exit(exit_callback)
				app_state["IS_RUNNING"] = False
		except TypeError as e:
			print("Type error: " + str(e))
		except ValueError as e:
			print("Value error: " + str(e))

def app_exit(exit_callback: callable):
	exit_callback()
	print(MSG_EXIT)


#==============____CLI____==============
#Command line interface
def cli_call_menu_start(start_callback: callable, login_functions: list) -> bool:
	if not callables(login_functions):
		return False
	start_callback()
	option: int = int(input(MENU_START))
	if option == 0:
		return False
	if option == 1:
		cli_call_menu_login(login_functions)
		return True
	raise ValueError(ERR_INVALID_OPTION)

def cli_call_menu_login(login_functions: list):
	option: int = -1
	while option != 0:
		option = int(input(MENU_LOGIN))
		if option == 0:
			return
		if option in range(1, 5):
			login_functions[option-1]()
		else:
			raise ValueError(ERR_INVALID_OPTION)


#============____STRINGS____============
MENU_START: str = """
==========
1. Log in
0. Exit
==========
"""

MENU_LOGIN: str = """
=================
1. Administrator
2. Doctor
3. Nurse
4. Patient
5. Receptionist
0. Back
=================
"""

ERR_INVALID_OPTION: str = "Invalid option. Try again."
ERR_PARAM_NOT_CALLABLE: str = "One or many callback parameters of app_run function are not callables"
ERR_MENU_ELEM_NOT_CALLABLE: str = "All list elements must be callables."

MSG_EXIT: str = "Application is shutting down..."

def str_add_extension_txt(filename: str) -> str:
	"""Adds '.txt' to the end of the file name."""
	return filename + ".txt"


#=============____FILES____=============
def file_create(filename: str) -> bool:
	"""
	Creates an empty text file if it doesn't exist.
	:param filename:
	:return: True if file was created successfully, else False
	"""
	try:
		with open(str_add_extension_txt(filename), 'r') as f:
			return False
	except FileNotFoundError:
		with open(str_add_extension_txt(filename), 'w') as f:
			return True

def file_read_str(filename: str) -> str:
	"""
	Reads the whole file as one string if file exists.
	:param filename: string. File name without extension.
	:return: string. File contents as a string.
	"""
	try:
		with open(str_add_extension_txt(filename), 'r') as f:
			return f.read()
	except FileNotFoundError:
		print('File not found. Please check the file path.')

def file_read_lines(filename: str) -> list:
	"""
	Reads the file line by line if file exists.
	:param filename: string. File name without extension.
	:return: list of strings. File contents as a list of lines.
	"""
	try:
		with open(str_add_extension_txt(filename), 'r') as f:
			return [line.strip() for line in f.readlines()]
	except FileNotFoundError:
		print('File not found. Please check the file path.')

def file_write_str(filename: str, content: str) -> bool:
	"""
	Adds a string to the end of the file. Creates a new file if it doesn't exist.
	:param filename: string. File name without extension.
	:param content: string to be appended to the end of the file.
	:return: True if string was written successfully, else False.
	"""
	with open(str_add_extension_txt(filename), 'a') as f:
		f.write(content)
		return True


def file_write_line(filename: str, content: str) -> bool:
	"""
	Adds a string and a new line to the end of the file. Creates a new file if it doesn't exist.
	:param filename: string. File name without extension.
	:param content: string to be appended to the end of the file.
	:return: True if string was written successfully, else False.
	"""
	return file_write_str(filename, content + "\n")