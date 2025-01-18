# Function to read a CSV file
def read_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            rows = content.split("\n")
            data = [row.split(",") for row in rows if row]  # Split rows into columns
            return data
    except FileNotFoundError:
        return []


# Function to write to a CSV file
def write_csv(file_name, data):
    try:
        with open(file_name, 'w') as file:
            for row in data:
                file.write(",".join(row) + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")


# Function to append to a CSV file
def append_to_csv(file_name, data):
    try:
        with open(file_name, 'a') as file:
            file.write(",".join(data) + "\n")
    except Exception as e:
        print(f"Error appending to file: {e}")


# Allows user to access and view personal medical records
def view_medical_records(patient_id):
    diagnosis_file = f"{patient_id}_diagnosis.csv"
    prescription_file = f"{patient_id}_prescription.csv"

    print("\n--- Medical Records ---")

    # Load diagnosis and prescription
    diagnosis = read_csv(diagnosis_file)
    prescription = read_csv(prescription_file)

    print("Diagnosis:")
    if diagnosis:
        for row in diagnosis:
            print(", ".join(row))
    else:
        print("No diagnosis records found.")

    print("\nPrescription:")
    if prescription:
        for row in prescription:
            print(", ".join(row))
    else:
        print("No prescription records found.")


# Function to view appointments
def view_appointments(patient_id):
    appointments_file = f"{patient_id}_appointments.csv"

    print("\n--- Appointments ---")
    appointments = read_csv(appointments_file)
    if appointments:
        print("Upcoming Appointments:")
        for row in appointments:
            print(", ".join(row))
    else:
        print("No upcoming appointments.")


# Function to schedule an appointment
def schedule_appointment(patient_id):
    appointments_file = f"{patient_id}_appointments.csv"

    try:
        # Ask user if they want to schedule a new appointment
        schedule_choice = input("\nWould you like to schedule a new appointment? (yes/no): ").lower()
        if schedule_choice == 'yes':
            # Schedule a new appointment
            appointment_details = input("Enter appointment details (date, time, doctor): ").split(", ")
            append_to_csv(appointments_file, appointment_details)
            print("Appointment scheduled successfully!")
        elif schedule_choice == 'no':
            print("No new appointment scheduled.")
        else:
            print("Invalid choice. Returning to the main menu.")
    except (ValueError, KeyboardInterrupt):
        print("\nError: Invalid input. Please enter a valid choice.")


# Main function to view and schedule appointments
def view_and_schedule_appointments(patient_id):
    view_appointments(patient_id)  # View existing appointments
    schedule_appointment(patient_id)  # Schedule a new appointment if the user chooses to do so


# Allows user to check and update personal information
def update_personal_info(patient_id):
    info_file = f"{patient_id}_info.csv"

    # Load current personal information
    personal_info = read_csv(info_file)

    print("\n--- Current Personal Information ---")
    if personal_info:
        for row in personal_info:
            print(", ".join(row))
    else:
        print("No personal information found.")

    try:
        # Asks user if they want to update their personal information
        update_choice = input("\nWould you like to update your personal information? (yes/no): ").lower()

        if update_choice == 'yes':
            print("\nEnter new information (Address, Contact Number, Insurance Details):")
            address = input("Address: ")
            contact_number = input("Contact Number: ")
            insurance_details = input("Insurance Details: ")

            new_info = [address, contact_number, insurance_details]

            write_csv(info_file, [new_info])
            print("Personal information updated successfully!")
        elif update_choice == 'no':
            print("No changes made to your personal information.")
        else:
            print("Invalid choice. Returning to the main menu.")
    except (ValueError, KeyboardInterrupt):
        print("\nError: Invalid input. Please enter a valid choice.")


# Allows user to request specific services
def request_service(patient_id):
    services_file = f"{patient_id}_services.csv"

    print("\n--- Request Specific Services ---")
    print("1. Follow-up Appointment")
    print("2. Request specific doctor")

    try:
        service_choice = input("Enter your choice (1/2): ")

        if service_choice == '1':
            service = "Follow-up Appointment"
        elif service_choice == '2':
            doctor_name = input("Enter doctor's name: ")
            service = f"Request specific doctor: {doctor_name}"
        else:
            print("Invalid choice. No service requested.")
            return

        append_to_csv(services_file, [service])
        print(f"Service '{service}' requested successfully!")
    except (ValueError, KeyboardInterrupt):
        print("\nError: Invalid input. Please enter a valid choice.")


# Allows user to view billing details
def view_billing_details(patient_id):
    billing_file = f"{patient_id}_billing.csv"

    print("\n--- Billing Details ---")
    billing_details = read_csv(billing_file)
    if billing_details:
        for row in billing_details:
            print(", ".join(row))
    else:
        print("No billing details found.")

    # View payment history
    payment_history_file = f"{patient_id}_payment_history.csv"
    print("\nPayment History:")
    payment_history = read_csv(payment_history_file)
    if payment_history:
        for row in payment_history:
            print(", ".join(row))
    else:
        print("No payment history found.")


# Main menu function
def main():
    print("Welcome to the Hospital Management System Patient Menu")
    try:
        patient_id = input("Please enter your patient ID: ")
    except (ValueError, KeyboardInterrupt):
        print("\nError: Invalid input. Exiting system.")
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