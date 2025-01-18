from datetime import datetime

import engine as e


#Load patient data from file
def load_patient_data(file_name):
  patient_data = {}
  try:
    with open(file_name, "r") as file:
      for line in file:
        line = line.strip()
        parts = line.split(", ")
        patient_id = parts[0]
        patient_name = parts[1]
        patient_age = int(parts[2])
        contact_number = parts[3]
        diagnosis = parts[4] if len(parts) > 4 else ""
        prescription = parts[5] if len(parts) > 5 else ""
        treatment_plan = parts[6] if len(parts) > 6 else ""
        appointment_date = parts[7] if len(parts) > 7 else ""
        if len(parts) > 8:
          medical_history = parts[8:-1]
          hospital_status = parts[-1]
        else:
          medical_history = []
          hospital_status = "Ongoing"

        patient_data[patient_id] = {
          "Name": patient_name,
          "Age": patient_age,
          "Contact Number": contact_number,
          "Diagnosis": diagnosis,
          "Prescription": prescription,
          "Treatment Plan": treatment_plan,
          "Appointment Date": appointment_date,
          "Medical History": medical_history,
          "Hospital Status": hospital_status
        }
  except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
  except Exception as e:
    print(f"An error occurred: {e}")
  return patient_data


#load doctor data from file
def load_doctor_data(file_name):
  doctor_data = {}
  try:
    with open(file_name, "r") as file:
      for line in file:
        line = line.strip()
        parts = line.split(", ")
        doctor_id = parts[0]
        doctor_name = parts[1]
        patients = parts[2].split(";") if len(parts) > 2 else []
        doctor_data[doctor_id] = {"Name": doctor_name, "Patients": patients}
  except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
  except Exception as e:
    print(f"An error occurred: {e}")
  return doctor_data


#View the assigned patients for doctor
def doctor_view_patients(doctor_id, doctor_data, patient_data):
  try:
    if doctor_id in doctor_data:
      doctor_info = doctor_data[doctor_id]
      print(f"\nDoctor: {doctor_info['Name']}")
      patient_list = doctor_info.get("Patients", [])

      if not patient_list:
        print("No patients assigned to this doctor.")
      else:
        print("\nAssigned Patients:")
        for patient_id in patient_list:
          if patient_id in patient_data:
            patient_info = patient_data[patient_id]
            print(f"Patient ID: {patient_id}")
            print(f"Name: {patient_info['Name']}")
            print(f"Age: {patient_info['Age']}")
            print(f"Contact Number: {patient_info['Contact Number']}")
            print("-" * 20)
          else:
            print(f"Patient ID: {patient_id} (Details not found)")
    else:
      print("Doctor ID not found.")

  except Exception as e:
    print(f"An error occurred: {e}")


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
  doctor_data = load_doctor_data(e.FILE_NAMES["DOCTORS"])
  patient_data = load_patient_data(e.FILE_NAMES["PATIENTS_DOCTOR"])

  doctor_show_list(doctor_data, patient_data)


#Upating the patient's record
def update_patient_record(patient_data, patient_id):

  if patient_id in patient_data:
    print(f"\nUpdating record for patient {patient_data[patient_id]['Name']} ({patient_id})")

    diagnosis = input("Enter diagnosis: ")
    prescription = input("Enter prescription: ")
    treatment_plan = input("Enter treatment plan: ")
    medical_history = input("Enter medical history (if applicable): ")

    patient_data[patient_id]["Diagnosis"] = diagnosis
    patient_data[patient_id]["Prescription"] = prescription
    patient_data[patient_id]["Treatment Plan"] = treatment_plan
    patient_data[patient_id]["Medical History"] = medical_history

    print(f"Record for patient {patient_data[patient_id]['Name']} updated successfully.")
  else:
    print("Patient ID not found. Please try again.")


#Saving the patient's data
def save_patient_data(file_name, patient_data):
  try:
    with open(file_name, "w") as file:
      for patient_id, data in patient_data.items():
        if isinstance(data['Medical History'], list):
          medical_history = ', '.join(data['Medical History'])
        else:
          medical_history = data['Medical History']

        line = f"{patient_id}, {data['Name']}, {data['Age']}, {data['Contact Number']}, {data['Diagnosis']}, {data['Prescription']}, {data['Treatment Plan']}, {data['Appointment Date']}, {medical_history}, {data['Hospital Status']}\n"
        file.write(line)
    print("Patient data saved successfully...")
  except Exception as e:
    print(f"An error occurred while saving patient data: {e}")


#Prompt patient ID for updating purposes
def patient_update_manager():
  file_name = e.FILE_NAMES["PATIENTS_DOCTOR"]

  patient_data = load_patient_data(file_name)

  while True:
    patient_id = input("\nEnter Patient ID to update record (or type 'exit' to quit): ")

    if patient_id.lower() == 'exit':
      print("Goodbye.")
      break

    update_patient_record(patient_data, patient_id)

    save_patient_data(file_name, patient_data)


#Scheduling appointment date
def doctor_appoints_patient(patient_data, patient_id, file_name):
  if patient_id in patient_data:
    print(f"\nScheduling a follow-up appointment for patient {patient_data[patient_id]['Name']} ({patient_id})")

    while True:
      appointment_date = input("Enter follow-up appointment date (YYYY-MM-DD): ").strip()

      try:
        datetime.strptime(appointment_date, "%Y-%m-%d")
        patient_data[patient_id]["Appointment Date"] = appointment_date
        print(
          f"Appointment for patient {patient_data[patient_id]['Name']} successfully scheduled for {appointment_date}.")

        save_patient_data(file_name, patient_data)
        break
      except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
  else:
    print("Patient ID not found. Please check the ID and try again.")


#Patient's full details
def view_patient_details(patient_data, patient_id):
  if patient_id in patient_data:
    patient = patient_data[patient_id]
    print(f"\n=== Details for {patient['Name']} ({patient_id}) ===")
    print(f"Age: {patient['Age']}")
    print(f"Contact Number: {patient['Contact Number']}")
    print(f"Diagnosis: {patient['Diagnosis']}")
    print(f"Prescription: {patient['Prescription']}")
    print(f"Treatment Plan: {patient['Treatment Plan']}")
    print(f"Appointment Date: {patient['Appointment Date']}")
    print("\nMedical History:")
    medical_history = [entry for entry in patient["Medical History"] if entry.strip()]  # Filter empty entries

    if not medical_history:
      print("  No medical history available.")
    else:
      for index, entry in enumerate(medical_history, start=1):
        print(f"  {index}. {entry}")
  else:
    print("Patient ID not found.")


#Doctor to view patient's full details
def doctor_view_menu():

  file_name = e.FILE_NAMES["PATIENTS_DOCTOR"]
  patient_data = load_patient_data(file_name)

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
  if patient_id in patient_data:
    patient = patient_data[patient_id]

    print(f"\nPatient: {patient['Name']} ({patient_id})")
    print(f"Diagnosis: {patient['Diagnosis']}")
    print(f"Treatment Plan: {patient['Treatment Plan']}")

    #Check patient has completed their treatment or is still under care
    if patient["Hospital Status"] == "Ongoing":
      recommendation = input(
        "The patient is still under treatment. Do you recommend a further stay? (yes/no): ").strip().lower()
      if recommendation == "yes":
        print(f"Recommendation: {patient['Name']} should remain in the hospital for further treatment.")
        patient_data[patient_id]["Hospital Status"] = "Further Stay Recommended"
      elif recommendation == "no":
        print(f"Discharge Approved: {patient['Name']} can be discharged.")
        patient_data[patient_id]["Hospital Status"] = "Discharged"
      else:
        print("Invalid input. Please respond with 'yes' or 'no'.")
    elif patient["Hospital Status"] == "Discharged":
      print(f"{patient['Name']} has already been discharged.")
    elif patient["Hospital Status"] == "Further Stay Recommended":
      print(f"{patient['Name']} has been recommended for further stay.")
  else:
    print("Patient ID not found.")

def patient_discharge_manager():
  file_name = e.FILE_NAMES["PATIENTS_DOCTOR"]
  patient_data = load_patient_data(file_name)

  while True:
    print("\nPatient Discharge Manager")
    patient_id = input("Enter Patient ID to update status (or type 'exit' to quit): ").strip()

    if patient_id.lower() == "exit":
      print("Exiting the program. Goodbye!")
      break

    issue_discharge_or_recommendation(patient_data, patient_id)
    save_patient_data(file_name, patient_data)


def main():
  doctor_file, patient_file = e.FILE_NAMES["DOCTORS"], e.FILE_NAMES["PATIENTS_DOCTOR"]
  doctor_data, patient_data = load_doctor_data(doctor_file), load_patient_data(patient_file)
  while True:
    print("\nDoctor's Menu:")
    print("1. View Personal Patient List")
    print("2. Update Patient Records")
    print("3. Schedule Follow-Up Appointments")
    print("4. View Medical History and Treatment Logs")
    print("5. Issue Discharge Approvals or Recommend Further Stay")
    print("6. Exit")
    choice = input("Select an option: ").strip()
    if choice == "1":
      launch_doctor_interface()
    elif choice == "2":
      patient_update_manager()
    elif choice == "3":
      patient_id = input("Enter the Patient ID to schedule an appointment: ").strip()
      doctor_appoints_patient(patient_data, patient_id, patient_file)
    elif choice == "4":
      doctor_view_menu()
    elif choice == "5":
      patient_discharge_manager()
    elif choice == "6":
      print("Exiting doctor menu...")
      break
    else:
      print("Invalid option. Try again.")

if __name__ == "__main__":
  main()
