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


 #def patient_update():
#   patient_ID = int((input("Enter patient_ID")))
#   if patient_ID in patient_data:
#     print("Current Information:" patient_data[patient_ID])
#     name = ("Enter New name: ")

#     while True:

