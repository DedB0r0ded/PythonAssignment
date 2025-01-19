from datetime import datetime

import engine


def display_menu():
  """Display the Nurse menu."""
  print("\n=== Hospital Management System - Nurse Menu ===")
  print("1. View Daily Patient List")
  print("2. Update Patient Vitals")
  print("3. Manage Medication Logs")
  print("4. Assist with Room Preparation")
  print("5. Report Emergency")
  print("6. Exit")
  choice = input("Enter your choice: ").strip()
  return choice


def view_daily_patient_list():
  """Access a daily list of patients and their required care."""
  print("\n--- Daily Patient List ---")
  try:
    medical_history = [m for m in engine.csv_read(engine.FILE_NAMES["MEDICAL_HISTORY"])]
    last_treated = [m['patient_id'] for m in medical_history if (datetime.strptime(m['date'].strip(), "%Y-%m-%d").date() == datetime.today().date())]
    patients = [p for p in engine.csv_read(engine.FILE_NAMES["PATIENTS"]) if (p["status"] == "hospitalized" and p["id"] not in last_treated)]
    if not patients:
      print("No patients to treat today.")
      return
    for p in patients:
      print(f"{p["id"]}. {p["name"]} - daily medical check-up required")

  except FileNotFoundError:
    print("Patient records not found.")
  #except ValueError:
    #print("File data format is invalid.")
  except IOError:
    print("An error occurred while accessing the patient file.")


def update_patient_vitals():
  """Update patient vitals and record observations."""
  print("\n--- Update Patient Vitals ---")
  patient_id = input("Enter Patient ID: ").strip()
  blood_pressure_sys = input("Enter Blood Pressure (systolic): ").strip()
  blood_pressure_dia = input("Enter Blood Pressure (diastolic): ").strip()
  heart_rate = input("Enter Heart Rate (bpm): ").strip()
  notes = input("Enter any notes about patient's state, if applicable: ").strip()

  if not (patient_id and blood_pressure_sys and blood_pressure_dia and heart_rate):
    print("All fields are required!")
    return

  try:
    engine.csv_write_medical_history({"patient_id": patient_id,
                                      "action": "Medical check-up",
                                      "date": datetime.today().strftime("%Y-%m-%d"),
                                      "HR": heart_rate, "notes": notes,
                                      "SYS": blood_pressure_sys,
                                      "DIA": blood_pressure_dia})
    print("Vitals updated successfully.")
  except FileNotFoundError:
    print("Vitals file not found.")
  except PermissionError:
    print("Permission denied while updating vitals.")
  except IOError:
    print("An I/O error occurred while updating vitals.")


def manage_medication_logs():
  """Manage medication logs and ensure timely administration."""
  print("\n--- Manage Medication Logs ---")
  medication = input("Enter Medication Name: ").strip()
  status = input("Enter Status (expired/ok): ").strip().lower()

  if status not in ["expired", "ok"]:
    print("Invalid status! Please enter 'expired' or 'ok'.")
    return

  try:
    engine.csv_write_medication_log({"name": medication, "date": datetime.now().date(), "status": status})
    print("Medication log updated successfully.")
  except FileNotFoundError:
    print("Medication logs file not found.")
  except PermissionError:
    print("Permission denied while updating medication logs.")
  except IOError:
    print("An I/O error occurred while updating medication logs.")


def assist_room_preparation():
  """Assist doctors by preparing rooms for treatment or surgical procedures."""
  print("\n--- Room Preparation ---")
  room_number = input("Enter Room Number: ").strip()
  task_details = input("Enter Task Details (e.g., prepare surgical equipment): ").strip()

  if not (room_number and task_details):
    print("Both Room Number and Task Details are required!")
    return

  try:
    engine.csv_write_room_prep({"user_id": None, "description": task_details, "room_id": room_number})
    print("Room preparation task logged successfully.")
  except FileNotFoundError:
    print("Room preparation file not found.")
  except PermissionError:
    print("Permission denied while updating room preparation file.")
  except IOError:
    print("An I/O error occurred while updating room preparation file.")


def report_emergency():
  """Report any medical emergencies to the assigned doctor."""
  print("\n--- Report Emergency ---")
  patient_id = input("Enter Patient ID: ").strip()
  emergency_details = input("Enter Emergency Details: ").strip()

  if not (patient_id and emergency_details):
    print("Patient ID and Emergency Details are required!")
    return

  patient = {}
  try:
    patient = [p for p in engine.csv_read(engine.FILE_NAMES["PATIENTS"]) if p["id"] == patient_id][0]
  except IndexError:
    print("Patient not found.")
    return
  engine.csv_write_medical_history({"patient_id": patient_id, "action": "Emergency!", "date": datetime.now().date(), "notes": emergency_details, "HR": None, "SYS": None, "DIA": None})
  print(f"Emergency reported for Patient ID {patient_id}: {emergency_details}")


def terminate_program():
  """Terminate the program gracefully."""
  print("\nThank you for using the Hospital Management System. Goodbye!")
  global running
  running = False


def main():
  """Main function to drive the Nurse menu."""
  global running
  running = True
  while running:
    choice = display_menu()
    if choice == "1":
      view_daily_patient_list()
    elif choice == "2":
      update_patient_vitals()
    elif choice == "3":
      manage_medication_logs()
    elif choice == "4":
      assist_room_preparation()
    elif choice == "5":
      report_emergency()
    elif choice == "6":
      terminate_program()
    else:
      print("Invalid choice. Please try again.")