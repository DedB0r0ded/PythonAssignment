# Function to register new patient
def register_patient():
    print("Register New Patient")
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    contact = input("Enter Contact Number: ")
    address = input("Enter Address: ")
    # Open the file and add patient data
    try:
        with open("patients.txt", "a") as file:
            file.write(f"{patient_id},{name},{contact},{address}\n")
        print("Patient Registered Successfully!")
    except Exception as e:
        print(f"Error registering patient: {e}")

# Function to schedule an appointment
def schedule_appointment():
    print("Schedule Appointment")
    patient_id = input("Enter Patient ID: ")
    doctor_name = input("Enter Doctor's Name: ")
    appointment_date = input("Enter Appointment Date (DD/MM/YYYY): ")
    try:
        with open("appointments.csv", "a") as file:
            file.write(f"{patient_id},{doctor_name},{appointment_date}\n")
        print("Appointment Scheduled Successfully!")
    except Exception as e:
        print(f"Error scheduling appointment: {e}")

# Function to manage patient check-in
def patient_check_in():
    print("Patient Check-In")
    patient_id = input("Enter Patient ID: ")
    try:
        with open("patients.txt", "r") as file:
            patients = file.readlines()
        found = False
        for patient in patients:
            if patient.split(",")[0] == patient_id:
                found = True
                break
        if found:
            with open("check_in.txt", "a") as file:
                file.write(f"{patient_id},Checked-In\n")
            print("Patient Checked In Successfully!")
        else:
            print("Patient ID not found.")
    except Exception as e:
        print(f"Error checking in patient: {e}")

# Function to manage patient check-out
def patient_check_out():
    print("Patient Check-Out")
    patient_id = input("Enter Patient ID: ")
    try:
        with open("check_in.txt", "r") as file:
            check_ins = file.readlines()
        found = False
        for check_in in check_ins:
            if check_in.split(",")[0] == patient_id:
                found = True
                break
        if found:
            with open("check_out.txt", "a") as file:
                file.write(f"{patient_id},Checked-Out\n")
            print("Patient Checked Out Successfully!")
        else:
            print("Patient ID not found in check-in records.")
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
        # Read all patients' data
        with open("patients.txt", "r") as file:
            patients = file.readlines()

        updated = False
        # Find the patient and update their details
        for i, patient in enumerate(patients):
            if patient.split(",")[0] == patient_id:
                updated = True
                print("Patient found!")
                # Get new details
                name = input("Enter new Name: ")
                contact = input("Enter new Contact Number: ")
                address = input("Enter new Address: ")
                # Update the patient details in the list
                patients[i] = f"{patient_id},{name},{contact},{address}\n"
                break
        
        if updated:
            # Write the updated patient list back to the file
            with open("patients.txt", "w") as file:
                file.writelines(patients)
            print("Patient information updated successfully!")
        else:
            print("Patient ID not found.")
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
