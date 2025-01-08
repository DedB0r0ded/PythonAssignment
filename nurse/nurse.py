import engine
from engine import PATIENTS_FILE, VITALS_FILE, MEDICATION_LOGS_FILE, ROOM_PREP_FILE


def initialize_files():
    """Ensure all necessary files exist."""
    for file in [PATIENTS_FILE, VITALS_FILE, MEDICATION_LOGS_FILE, ROOM_PREP_FILE]:
        try:
            open(file, "x").close() 
        except FileExistsError:
            pass 


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
        with open(PATIENTS_FILE, "r") as file:
            patients = file.readlines()
            if not patients:
                print("No patients found.")
            else:
                for patient in patients:
                    patient_id, name, care_required = patient.strip().split("|")
                    print(f"ID: {patient_id}, Name: {name}, Care Required: {care_required}")
    except FileNotFoundError:
        print("Patient records not found.")


def update_patient_vitals():
    """Update patient vitals and record observations."""
    print("\n--- Update Patient Vitals ---")
    patient_id = input("Enter Patient ID: ").strip()
    temperature = input("Enter Temperature (°C): ").strip()
    blood_pressure = input("Enter Blood Pressure (e.g., 120/80): ").strip()
    heart_rate = input("Enter Heart Rate (bpm): ").strip()

    if not (patient_id and temperature and blood_pressure and heart_rate):
        print("All fields are required!")
        return

    try:
        with open(VITALS_FILE, "a") as file:
            file.write(f"{patient_id}|{temperature}|{blood_pressure}|{heart_rate}\n")
        print("Vitals updated successfully.")
    except Exception as e:
        print(f"Error updating vitals: {e}")


def manage_medication_logs():
    """Manage medication logs and ensure timely administration."""
    print("\n--- Manage Medication Logs ---")
    patient_id = input("Enter Patient ID: ").strip()
    medication = input("Enter Medication Name: ").strip()
    status = input("Enter Status (Administered/Skipped): ").strip().lower()

    if status not in ["administered", "skipped"]:
        print("Invalid status! Please enter 'Administered' or 'Skipped'.")
        return

    try:
        with open(MEDICATION_LOGS_FILE, "a") as file:
            file.write(f"{patient_id}|{medication}|{status}\n")
        print("Medication log updated successfully.")
    except Exception as e:
        print(f"Error updating medication logs: {e}")


def assist_room_preparation():
    """Assist doctors by preparing rooms for treatment or surgical procedures."""
    print("\n--- Room Preparation ---")
    room_number = input("Enter Room Number: ").strip()
    task_details = input("Enter Task Details (e.g., prepare surgical equipment): ").strip()

    if not (room_number and task_details):
        print("Both Room Number and Task Details are required!")
        return

    try:
        with open(ROOM_PREP_FILE, "a") as file:
            file.write(f"Room {room_number}|{task_details}\n")
        print("Room preparation task logged successfully.")
    except Exception as e:
        print(f"Error logging room preparation: {e}")


def report_emergency():
    """Report any medical emergencies to the assigned doctor."""
    print("\n--- Report Emergency ---")
    patient_id = input("Enter Patient ID: ").strip()
    emergency_details = input("Enter Emergency Details: ").strip()

    if not (patient_id and emergency_details):
        print("Patient ID and Emergency Details are required!")
        return

    print(f"Emergency reported for Patient ID {patient_id}: {emergency_details}")


def terminate_program():
    """Terminate the program gracefully."""
    print("\nThank you for using the Hospital Management System. Goodbye!")
    exit()


def main():
    """Main function to drive the Nurse menu."""
    initialize_files()
    while True:
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
