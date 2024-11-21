from operator import concat

import engine
#done TODO: Remove global variables - make them local
#done TODO: C from CRUD - create. patient_create(name, age, contact, ...) -> patient; clui_patient_create();
# TODO: R from CRUD - read. patient_read(id) -> patient; patients_read() -> [patient, patient, ...]; clui_patient_read(); clui_patients_read()
# TODO: change `patient_data` dict to `patients` list
# TODO: remove capitals from dictionary keys naming (Name > name, Age > age, ...)
# TODO: make all backend functions work with csv files using engine module
#2 0f 3TODO: U from CRUD - update. patient_update(id, name, age, ...) -> patient; patient_save(patient); interface_patient_update()
# doneTODO: D from CRUD - delete. patient_delete(id) -> patient; clui_patient_delete()


def patient_validate_id(patient_data, patient_id: int):
  if  patient_id in patient_data:
    raise ValueError("There is no patient with this id.")


def validate_name(name: str):
    if not name or name == "":
      raise ValueError("Invalid name.")


def validate_age(age: str):
  try:
    age = int(age)
  except ValueError:
    raise ValueError("Invalid age format.")
  if not age:
    raise ValueError("There is no patient age.")
  return age

def patient_validate_contact(contact: str):
  if contact and contact[0] == "+":
    contact = contact[1:]
  return contact.isdigit() and 9 <= len(contact) <= 12

  pass


# -------------------------------------------CUD Operations----------------------------

def patient_create(patient_data, name, age, contact):
  validate_name(name)
  age = validate_age(age)
  contact = patient_validate_contact(contact)

  patient_id = len(patient_data) + 1

  patient_data[patient_id] = {"name":name ,"age": age ,"contact number":contact }
  print(f"New patient {name} registered successfully")



def patient_update(patient_data,patient_id,name,age,contact):
  try:
    patient_validate_id(patient_data, patient_id)
  except ValueError:
    print("Patient ID not found. Please check and try again.")
    return
  patient = patient_data[patient_id]

  if name:
    validate_name(name)
    patient["name"] = name.upper()
  if  age:
    patient["age"] = validate_age(age)
  if  contact:
    patient["contact"] = patient_validate_contact(contact)

  print(f"Patient ID {patient_id} updated successfully.")
  return patient_data[patient_id]
  pass


def patient_delete(patient_data, patient_id):
  patient_validate_id(patient_data, patient_id)
  remove = patient_data.pop(patient_id)
  print(f"Patient ID {patient_id} deleted successfully.")
  return remove



def patient_save(patient):
  #Saves into a file
  pass


# -----------------------------CLUI functions--------------------------

def clui_patient_create(patient_data):
  name = input("Enter Patient Name: ")
  age = input("Enter Patient Age: ")
  contact = input("Enter Patient Contact Number: ")
  return patient_create(patient_data, name, age, contact)


def clui_patient_update(patient_data):
  try:
    patient_id = int(input("Enter patient ID to update: "))
    if patient_id in patient_data:
      print("Current Information:", patient_data[patient_id])
    else:
      print("Patient ID not found.")
      return
    name = input("Enter new name (leave blank to skip): ")
    age = input("Enter new age (leave blank to skip): ")
    contact = input("Enter new contact number  (leave blank to skip): ")
    return patient_update(patient_data, name, age, contact)
  except ValueError:
    print("Invalid input. Please enter a valid patient ID and try again.")


def clui_patient_delete(patient_data):
    try:
      patient_id = int(input("Enter Patient ID to delete: "))
      patient_delete(patient_data, patient_id)
    except ValueError:
      print("Invalid input. Please enter a valid patient ID and try again.")

#--------------------------------------------------------------------------

def main():
  patient_data = {}
  while True:
    print("Patient Management System")
    print("1. Register Patient")
    print("2. Update Patient  ")
    print("3. Delete Patient  ")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice =="1":
      clui_patient_create(patient_data)

    elif choice =="2":
      clui_patient_update(patient_data)

    elif choice =="3":
      clui_patient_delete(patient_data)
    elif choice =="4":
      print("Exiting the system. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again. ")


main()






