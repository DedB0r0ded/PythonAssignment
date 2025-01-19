import engine

PATIENTS_FILE_NAME = engine.FILE_NAMES["PATIENTS"]
SERVICES_FILE_NAME = engine.FILE_NAMES["SERVICES"]


def create_appointment(patient_id):
    date, doctor_id = input("Enter appointment details (date, doctor id): ").split(", ")
    doctors = [d for d in engine.csv_read(engine.FILE_NAMES["DOCTORS"]) if doctor_id == d["id"]]
    if not doctors:
        raise ValueError("Doctor with this id does not exist")
    description = input("Enter appointment description: ")
    return {
        "doctor_id": doctor_id,
        "patient_id": patient_id,
        "date": date,
        "description": description,
        "status": "payment_pending",
        "is_appointment": True
    }


# Allows user to access and view personal medical records
def view_medical_records(patient_id):
    print("\n--- Medical Records ---")

    patients = [p for p in engine.csv_read(PATIENTS_FILE_NAME) if p["id"] == patient_id]
    for patient in patients:
        print(f"Diagnosis: {patient['diagnosis']}, Prescription: {patient['diagnosis']}, Treatment Plan: {patient['treatment_plan']}")


# Function to view appointments
def view_appointments():
    doctors_file = engine.FILE_NAMES["DOCTORS"]

    print("\n--- Appointments ---")
    services = engine.csv_read(SERVICES_FILE_NAME)
    doctors = engine.csv_read(doctors_file)

    for service in services:
        if service['is_appointment']:
            doctor = [d for d in doctors if d["id"] == service["doctor_id"]][0]
            print(f"Doctor: {doctor['name']}, Date: {service['date']}, Description: {service['description']}, Status: {service['status']}")


# Function to schedule an appointment
def schedule_appointment(patient_id):
    try:
        # Ask user if they want to schedule a new appointment
        schedule_choice = input("\nWould you like to schedule a new appointment? (yes/no): ").lower()
        if schedule_choice == 'yes':
            # Schedule a new appointment

            new_appointment = create_appointment(patient_id)
            service_id = engine.csv_write_service(new_appointment)
            new_billing = {"patient_id": patient_id, "service_id": service_id, "total": 600, "paid": 0, "date": new_appointment["date"]}
            engine.csv_write_billing(new_billing)
            print("Appointment scheduled successfully!")
        elif schedule_choice == 'no':
            print("No new appointment scheduled.")
        else:
            print("Invalid choice. Returning to the main menu.")
    except ValueError as e:
        print(e)


# Main function to view and schedule appointments
def view_and_schedule_appointments(patient_id):
    view_appointments()  # View existing appointments
    schedule_appointment(patient_id)  # Schedule a new appointment if the user chooses to do so


# Allows user to check and update personal information
def update_personal_info(patient_id):
    # Load current personal information
    patients = engine.csv_read(PATIENTS_FILE_NAME)
    patient = [p for p in patients if patient_id == p["id"]][0]

    print("\n--- Current Personal Information ---")
    print(f"Name: {patient['name']}, Age: {patient['age']}, Phone number: {patient['phone_number']}, Address: {patient['address']}")

    try:
        # Asks user if they want to update their personal information
        update_choice = input("\nWould you like to update your personal information? (yes/no): ").lower()

        if update_choice == 'yes':
            print("\nEnter new information (Name, Age, Address, Contact Number): ")
            name = input("Name: ")
            age = input("Age: ")
            number = input("Number: ")
            address = input("Address: ")

            patient.update({"name": name, "age": age, "address": address, "number": number})
            patients_new = [patient if p["id"] == patient_id else p for p in patients]
            engine.csv_rewrite(PATIENTS_FILE_NAME, patients_new)

            print("Personal information updated successfully!")
        elif update_choice == 'no':
            print("No changes made to your personal information.")
        else:
            print("Invalid choice. Returning to the main menu.")
    except (ValueError, KeyboardInterrupt):
        print("\nError: Invalid input. Please enter a valid choice.")


# Allows user to request specific services
def request_service(patient_id):
    print("\n--- Request follow-up appointment with specific doctor ---")
    try:
        follow_up_appointment = create_appointment(patient_id)
        service_id = engine.csv_write_service(follow_up_appointment)
        new_billing = {"patient_id": patient_id, "service_id": service_id, "total": 600, "paid": 0, "date": follow_up_appointment["date"]}
        engine.csv_write_billing(new_billing)
        print("Follow-up appointment was scheduled successfully!")
    except (ValueError, KeyboardInterrupt):
        print("\nError: Invalid input. Please enter a valid choice.")


# Allows user to view billing details
def view_billing_details(patient_id):
    billing_file = engine.FILE_NAMES["BILLING"]

    print("\n--- Billing Details ---")
    for billing in [b for b in engine.csv_read(billing_file) if b["patient_id"] == patient_id]:
        service_description = [s for s in engine.csv_read(SERVICES_FILE_NAME) if s["id"] == billing["service_id"]][0]["description"]
        patient_name = [p for p in engine.csv_read(PATIENTS_FILE_NAME) if p["id"] == billing["patient_id"]][0]["name"]
        print(f"Patient Name: {patient_name}, Description: {service_description}, Total: {billing['total']}, Paid: {billing['paid']}, Date: {billing['date']}")


# Main menu function
def main():
    print("Welcome to the Hospital Management System Patient Menu")
    try:
        patient_id = input("Please enter your patient ID: ")
        patient = [p for p in engine.csv_read(PATIENTS_FILE_NAME) if patient_id == p["id"]]
        if not patient:
            raise ValueError("Error. Patient with this id does not exist")
    except ValueError as e:
        print(e)
        return

    while True:
        print("\n--- Main Menu ---")
        print("1. View Medical Records")
        print("2. View and Schedule Appointments")
        print("3. Update Personal Information")
        print("4. Request Specific Services")
        print("5. View Billing Details")
        print("6. Exit")

        try:
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                view_medical_records(patient_id)
            elif choice == '2':
                view_and_schedule_appointments(patient_id)
            elif choice == '3':
                update_personal_info(patient_id)
            elif choice == '4':
                request_service(patient_id)
            elif choice == '5':
                view_billing_details(patient_id)
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except (ValueError, KeyboardInterrupt):
            print("\nError: Invalid input. Please enter a valid choice.")


if __name__ == "__main__":
    main()
