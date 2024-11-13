patient_data = {}
def patient_create():
  while True:
    try:
      patient_ID = int(input("Enter patient_ID: "))
      break
    except ValueError:
      print("Invalid input. Please Enter Patient_ID:")
  if patient_ID in patient_data:
    print("This patient already exists. Try updating instead. ")
  else:
    name = input("Enter Patient Name: ").upper()

    while True:
      try:
        age = int(input("Enter Patient Age: "))
        break
      except ValueError:
        print("Invalid input. Please Enter Patient Age:")

    while True:
      try:
        contact = int(input("Enter Patient Contact Number:"))
        break
      except ValueError:
        print("Invalid input. Please Enter Contact Number:")

  patient_data[patient_ID] = {"Name":name ,"Age": age ,"Contact Number":contact }
  print(f"New patient {name} registered successfully")

#-------------------------------------------------------------

def patient_update():
  patient_ID = int(input("Enter patient_ID: "))
  if patient_ID in patient_data:
    print("Current Information: ", patient_data[patient_ID])
    name = input("Enter New Name: ")

    while True:
      try:
        age = int(input("Enter Patient Age: "))
        break
      except ValueError:
        print("Invalid input. please enter age")

    while True:
      try:
        contact = int(input("Enter Patient Contact Number: "))
        break
      except ValueError:
        print("Invalid input. please enter Contact Number.")

    if name:
      patient_data[patient_ID]["Name"] = name

    if age:
      patient_data[patient_ID]["Age"] = age

    if contact:
      patient_data[patient_ID]["Contact Number"] = contact

    print("Patient information updated successfully!")
  else:
    print("Patient ID not found. Please register first.")

#--------------------------------------------------------------------------

def main():
  while True:
    print("Patient Management System")
    print("1. Register Patient")
    print("2. Update Patient  ")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":
      patient_create()

    elif choice =="2":
      patient_update()

    elif choice =="3":
      print("Exiting the system. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again. ")








