user_db = {} #User database: contains the user name and password
doctor_db = {} #Doctors database: contains the name of the doctor and his available appointments
appointments_db = [] #Booked appointments database

def  register_user (username,password):
    if username in user_db:
        return "Username already taken."
    user_db[username] = password
    return f"User {username} registered successfully."

while True:
    username = input("Enter username: ")
    password = (input("Enter password"))
    print(register_user(username, password))
    continue_choice = input("Do you want to add another user? (yes/no): ")
    if continue_choice.lower() != "yes":
        break

print(user_db)
#----------------------------------------------------------------------------------------------

def login_user(username,password):
    if user_db.get(username) == password:
        return f"Welcome {username} "
    else:
        return "Incorrect username or password."




