from ctypes import pydll
from datetime import datetime

import engine
from engine import csv_write_patient


def find_patient(patient_id):
  patients = [p for p in engine.csv_read(engine.FILE_NAMES["PATIENTS"])]
  try:
    patient = [p for p in patients if patient_id == p["id"]][0]
    return patient
  except IndexError:
    return


# Function to register new patient
def register_patient():
  print("Register New Patient")
  age = input("Enter Patient Age: ")
  name = input("Enter Patient Name: ")
  contact = input("Enter Contact Number: ")
  address = input("Enter Address: ")
  # Open the file and add patient data
  try:
    csv_write_patient({"user_id": None, "name": name, "age": age, "phone_number": contact, "address": address, "status": None})
    print("Patient Registered Successfully!")
  except Exception as e:
    print(f"Error registering patient: {e}")


# Function to schedule an appointment
def schedule_appointment():
  patient_id = input("Enter the Patient ID to schedule an appointment: ").strip()
  doctor_id = input("Enter the Doctor ID to schedule an appointment: ").strip()
  patients = [p for p in engine.csv_read(engine.FILE_NAMES["PATIENTS"])]
  doctors = [p for p in engine.csv_read(engine.FILE_NAMES["DOCTORS"])]
  patient = [p for p in patients if p["id"] == patient_id][0]
  doctor = [p for p in doctors if p["id"] == doctor_id][0]
  if not patient:
    print("Patient ID not found. Please check the ID and try again.")
    return
  while True:
    appointment_date = input("Enter follow-up appointment date (YYYY-MM-DD): ").strip()
    try:
      datetime.strptime(appointment_date, "%Y-%m-%d")
      service_id = engine.csv_write_service({"doctor_id": doctor_id, "patient_id": patient_id, "date": appointment_date,
                                      "description": f"Appointment for patient {patient['name']} ({patient_id}) from Doctor {doctor['name']} ({doctor_id})",
                                      "status": "payment_pending", "is_appointment": True})
      engine.csv_write_billing(
        {"patient_id": patient_id, "service_id": service_id, "total": 600, "paid": 0, "date": datetime.now().date()})
      print(f"Appointment for patient {patient['name']} successfully scheduled for {appointment_date}.")
      break
    except ValueError:
      print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


# Function to manage patient check-in
def patient_check_in():
  print("Patient Check-In")
  patient_id = input("Enter Patient ID: ")
  try:
    patient = {}
    patients = [p for p in engine.csv_read(engine.FILE_NAMES["PATIENTS"])]
    try:
      patient = [p for p in patients if patient_id == p["id"]][0]
    except IndexError:
      print("Patient ID not found.")
      return
    patient["status"] = "hospitalized"
    patients_new = [patient if p["id"] == patient_id else p for p in patients]
    engine.csv_rewrite(engine.FILE_NAMES["PATIENTS"], patients_new)
    print("Patient Checked In!")
  except Exception as e:
    print(f"Error checking in patient: {e}")


# Function to manage patient check-out
def patient_check_out():
  print("Patient Check-Out")
  patient_id = input("Enter Patient ID: ")
  try:
    patient = {}
    patients = [p for p in engine.csv_read(engine.FILE_NAMES["PATIENTS"])]
    try:
      patient = [p for p in patients if patient_id == p["id"]][0]
    except IndexError:
      print("Patient ID not found.")
      return
    patient["status"] = "discharged"
    patients_new = [patient if p["id"] == patient_id else p for p in patients]
    engine.csv_rewrite(engine.FILE_NAMES["PATIENTS"], patients_new)
    print("Patient Checked Out!")
  except Exception as e:
    print(f"Error checking out patient: {e}")


# Function to generate billing details
def generate_billing():
  print("Generate Billing Details")
  patient_id = input("Enter Patient ID: ")
  service_details = input("Enter Service Used (e.g., consultation, tests): ")
  amount = input("Enter Amount: ")
  try:
    with open("billing.txt", "a") as file:
      file.write(f"{patient_id},{service_details},{amount}\n")
    print("Billing Details Generated Successfully!")
  except Exception as e:
    print(f"Error generating billing details: {e}")


# Function to update existing patient information
def update_patient():
  print("Update Patient Information")
  patient_id = input("Enter Patient ID to update: ")
  try:
    patient = find_patient(patient_id)
    patient["age"] = input("Enter New Age: ")
    patient["name"] = input("Enter New Name: ")
    patient["phone_number"] = input("Enter New Number: ")
    patient["address"] = input("Enter New Address: ")
    patients = engine.csv_read(engine.FILE_NAMES["PATIENTS"])
    patients_new = [patient if p["id"] == patient_id else p for p in patients]
    engine.csv_rewrite(engine.FILE_NAMES["PATIENTS"], patients_new)
  except Exception as e:
    print(f"Error updating patient information: {e}")


# Modify the receptionist menu to include the update option
def receptionist_menu():
  while True:
    print("\n--- Receptionist Menu ---")
    print("1. Register New Patient")
    print("2. Schedule Appointment")
    print("3. Check-In Patient")
    print("4. Check-Out Patient")
    print("5. Generate Billing Details")
    print("6. Update Patient Information")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
      register_patient()
    elif choice == "2":
      schedule_appointment()
    elif choice == "3":
      patient_check_in()
    elif choice == "4":
      patient_check_out()
    elif choice == "5":
      generate_billing()
    elif choice == "6":
      update_patient()
    elif choice == "7":
      print("Exiting...")
      break
    else:
      print("Invalid choice! Please try again.")