# Function to view assigned patients for a doctor
def view_assigned_patients(doctor_ID, doctor_data, patient_data):
    try:
        if doctor_ID in doctor_data:
            doctor_info = doctor_data[doctor_ID]
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
            print("Doctor ID not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    while True:
        print("\nDoctor's Assigned Patient List")
        doctor_id_input = input("Enter Doctor ID to view assigned patients (or type 'exit' to quit): ")
        if doctor_id_input.lower() == 'exit':
            print("Goodbye")
            break
        view_assigned_patients(doctor_id_input, doctor_data, patient_data)

main()
