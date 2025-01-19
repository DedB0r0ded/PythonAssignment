from datetime import datetime

import engine
from engine import csv_write_service, csv_write_billing


#Load patient data from file
def load_patient_data():
  patient_data = engine.csv_read(engine.FILE_NAMES["PATIENTS"])
  return patient_data


#load doctor data from file
def load_doctor_data():
  doctor_data = engine.csv_read(engine.FILE_NAMES["DOCTORS"])
  return doctor_data


#Sacing the medical history data
def save_medical_history_record(record):
  old = engine.csv_read(engine.FILE_NAMES["MEDICAL_HISTORY"])
  new = [m if m["id"] != record["id"] else record for m in old]
  engine.csv_rewrite(engine.FILE_NAMES["MEDICAL_HISTORY"], new)


#Saving the patient's data
def save_patient_data(patient_data):
  try:
    engine.csv_rewrite(engine.FILE_NAMES["PATIENTS"], patient_data)
  except Exception as e:
    print(f"An error occurred while saving patient data: {e}")


#View the assigned patients for doctor
def doctor_view_patients(doctor_id, doctor_data, patient_data):
  services = engine.csv_read(engine.FILE_NAMES["SERVICES"])
  appointments = [s for s in services if s["is_appointment"] and s["doctor_id"] == doctor_id]
  patient_ids = [a["patient_id"] for a in appointments]
  patients = [p for p in engine.csv_read(engine.FILE_NAMES["PATIENTS"]) if p["id"] in patient_ids]
  if not patients:
    print("No patients assigned to this doctor.")
  else:
    print("\nAssigned Patients:")
    for patient in patients:
      print(f"Patient ID: {patient['id']}",sep="",end="; ")
      print(f"Name: {patient['name']}",sep="",end="; ")
      print(f"Age: {patient['age']}",sep="",end="; ")
      print(f"Contact Number: {patient['phone_number']}",sep="",end=".\n")


#Prompt the doctor ID and view assigned patients
def doctor_show_list(doctor_data, patient_data):
  while True:
    print("\nDoctor's Assigned Patient List")
    doctor_id = input("Enter Doctor ID to view assigned patients (or type 'exit' to quit): ")
    if doctor_id.lower() == 'exit':
      print("Goodbye")
      break
    else:
      doctor_view_patients(doctor_id, doctor_data, patient_data)


#Doctor's Interface
def launch_doctor_interface():
  doctor_data = load_doctor_data()
  patient_data = load_patient_data()

  doctor_show_list(doctor_data, patient_data)


#Upating the patient's record
def update_patient_record(patient_data, patient_id):
  patient_ids = [p["id"] for p in patient_data]
  if patient_id in patient_ids:
    patient = [p for p in patient_data if p["id"] == patient_id][0]
    print(f"\nUpdating record for patient {patient['name']} ({patient_id})")

    diagnosis = input("Enter diagnosis: ")
    prescription = input("Enter prescription: ")
    treatment_plan = input("Enter treatment plan: ")

    patient["diagnosis"] = diagnosis
    patient["prescription"] = prescription
    patient["treatment_plan"] = treatment_plan

    print(f"Record for patient {patient['name']} updated successfully.")
    patient_data_new = [patient if p["id"] == patient_id else p for p in patient_data]
    save_patient_data(patient_data_new)
  else:
    print("Patient ID not found. Please try again.")


#Prompt patient ID for updating purposes
def patient_update_manager():
  patient_data = load_patient_data()
  while True:
    patient_id = input("\nEnter Patient ID to update record (or type 'exit' to quit): ")

    if patient_id.lower() == 'exit':
      print("Goodbye.")
      break

    update_patient_record(patient_data, patient_id)


#Scheduling appointment date
def doctor_appoints_patient(patient_data, doctor_data):
  patient_id = input("Enter the Patient ID to schedule an appointment: ").strip()
  doctor_id = input("Enter the Doctor ID to schedule an appointment: ").strip()
  patient = [p for p in patient_data if p["id"] == patient_id][0]
  doctor = [p for p in doctor_data if p["id"] == doctor_id][0]
  if not patient:
    print("Patient ID not found. Please check the ID and try again.")
    return
  while True:
    appointment_date = input("Enter follow-up appointment date (YYYY-MM-DD): ").strip()
    try:
      datetime.strptime(appointment_date, "%Y-%m-%d")
      service_id = csv_write_service({"doctor_id": doctor_id, "patient_id": patient_id, "date": appointment_date, "description": f"Appointment for patient {patient['name']} ({patient_id}) from Doctor {doctor['name']} ({doctor_id})","status":"payment_pending","is_appointment":True})
      csv_write_billing({"patient_id": patient_id, "service_id": service_id, "total": 600, "paid": 0, "date": datetime.now().date()})
      print(f"Appointment for patient {patient['name']} successfully scheduled for {appointment_date}.")
      break
    except ValueError:
      print("Invalid date format. Please enter the date in YYYY-MM-DD format.")


#Patient's full details
def view_patient_details(patient_data, patient_id):
  patient = [p for p in patient_data if p["id"] == patient_id][0]
  if not patient:
    print("Patient ID not found.")
    return
  print(f"\n=== Details for {patient['name']} ({patient_id}) ===")
  print(f"Age: {patient['age']}")
  print(f"Contact Number: {patient['phone_number']}")
  print(f"Diagnosis: {patient['diagnosis']}")
  print(f"Prescription: {patient['prescription']}")
  print(f"Treatment Plan: {patient['treatment_plan']}")
  print("\nMedical History:")
  medical_history = [entry for entry in engine.csv_read(engine.FILE_NAMES["MEDICAL_HISTORY"]) if entry["patient_id"] == patient_id]  # Filter empty entries

  if not medical_history:
    print("  No medical history available.")
  else:
    for index, entry in enumerate(medical_history, start=1):
      print(f"  {index}. {entry["date"]} - {entry['action']}; HR: {entry['HR']}, SYS: {entry['SYS']}, DIA: {entry['DIA']}")


#Doctor to view patient's full details
def doctor_view_menu(patient_data):
  while True:
    print("\n=== Doctor's Patient Management Menu ===")
    print("1. View Medical History and Treatment Logs")
    print("2. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
      patient_id = input("\nEnter Patient ID to view details: ").strip()
      view_patient_details(patient_data, patient_id)
    elif choice == "2":
      print("Exiting Doctor's Patient Management Menu. Goodbye.")
      break
    else:
      print("Invalid choice. Please try again.")


#Doctor recommend patient to discharge or stay further based on treatment status
def issue_discharge_or_recommendation(patient_data, patient_id):
  patient = [p for p in patient_data if p["id"] == patient_id][0]

  if not patient:
    print("Patient ID not found.")
    return

  print(f"\nPatient: {patient['name']} ({patient_id})")
  print(f"Diagnosis: {patient['diagnosis']}")
  print(f"Treatment Plan: {patient['treatment_plan']}")

  #Check patient has completed their treatment or is still under care
  if patient["status"] == "hospitalized":
    recommendation = input(
      "The patient is still under treatment. Do you recommend a further stay? (yes/no): ").strip().lower()
    if recommendation == "yes":
      print(f"Recommendation: {patient['name']} should remain in the hospital for further treatment.")
      patient["status"] = "hospitalized"
    elif recommendation == "no":
      print(f"Discharge Approved: {patient['name']} can be discharged.")
      patient["status"] = "discharged"
    else:
      print("Invalid input. Please respond with 'yes' or 'no'.")
  elif patient["status"] == "discharged":
    print(f"{patient['name']} has already been discharged.")
  patient_data_new = [patient if p["id"] == patient_id else p for p in patient_data]
  save_patient_data(patient_data_new)


def patient_discharge_manager(patient_data):
  while True:
    print("\nPatient Discharge Manager")
    patient_id = input("Enter Patient ID to update status (or type 'exit' to quit): ").strip()
    if patient_id.lower() == "exit":
      print("Exiting the program. Goodbye!")
      break
    issue_discharge_or_recommendation(patient_data, patient_id)


def main():
  doctors, patients = load_doctor_data(), load_patient_data()
  while True:
    print("\nDoctor's Menu:")
    print("1. View Personal Patient List")
    print("2. Update Patient Records")
    print("3. Schedule Follow-Up Appointments")
    print("4. View Medical History and Treatment Logs")
    print("5. Issue Discharge Approvals or Recommend Further Stay")
    print("6. Log out")
    choice = input("Select an option: ").strip()
    if choice == "1":
      launch_doctor_interface()
    elif choice == "2":
      patient_update_manager()
    elif choice == "3":
      doctor_appoints_patient(patients, doctors)
    elif choice == "4":
      doctor_view_menu(patients)
    elif choice == "5":
      patient_discharge_manager(patients)
    elif choice == "6":
      print("Exiting doctor menu...")
      break
    else:
      print("Invalid option. Try again.")
