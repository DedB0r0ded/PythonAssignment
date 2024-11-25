import datetime

# List to store patient data
patients = [
    {"id": 1, "name": "lily wayne", "care": "Routine Check-up", "vitals": {}, "observations": []},
    {"id": 2, "name": "mark webber", "care": "Post-surgery Observation", "vitals": {}, "observations": []},
    {"id": 3, "name": "max verstrappen", "care": "Physical Therapy", "vitals": {}, "observations": []},
]


def display_patient_list():
    print("\n--- Daily Patient List ---")
    for patient in patients:
        print(f"ID: {patient['id']}, Name: {patient['name']}, Care: {patient['care']}")
    print("--------------------------")


def find_patient(patient_id):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    return None


def update_vitals():
    try:
        patient_id = int(input("\nEnter Patient ID to update vitals: "))
        patient = find_patient(patient_id)
        if patient:
            print(f"Updating vitals for {patient['name']}")
            vitals = {
                "Temperature (°C)": input("Enter Temperature (°C): "),
                "Blood Pressure (mmHg)": input("Enter Blood Pressure (mmHg): "),
                "Heart Rate (bpm)": input("Enter Heart Rate (bpm): "),
            }
            patient["vitals"] = vitals
            print("Vitals updated successfully.")
        else:
            print("Patient not found. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric Patient ID.")


def record_observations():
    try:
        patient_id = int(input("\nEnter Patient ID to record observations: "))
        patient = find_patient(patient_id)
        if patient:
            observation = input(f"Enter observation for {patient['name']}: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            patient["observations"].append({"timestamp": timestamp, "note": observation})
            print("Observation recorded successfully.")
        else:
            print("Patient not found. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric Patient ID.")


def terminate_program():
    print("\nExiting the program. Goodbye!")


def main():
    while True:
        print("\n--- Patient Management System ---")
        print("1. View Daily Patient List")
        print("2. Update Patient Vitals")
        print("3. Record Observations")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_patient_list()
        elif choice == "2":
            update_vitals()
        elif choice == "3":
            record_observations()
        elif choice == "4":
            terminate_program()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()