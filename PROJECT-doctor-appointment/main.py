import csv
import os
import random
import hashlib
from voice_engine import speak, get_hybrid_input

# --- Absolute File Paths Fix ---
# This forces the CSV files to ALWAYS save in the exact same folder as main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DOCTORS = os.path.join(BASE_DIR, "doctors.csv")
FILE_PATIENTS = os.path.join(BASE_DIR, "patients.csv")
FILE_APPTS = os.path.join(BASE_DIR, "appointments.csv")

# --- Security ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- Database Initialization ---
def init_db():
    if not os.path.exists(FILE_DOCTORS) or os.stat(FILE_DOCTORS).st_size == 0:
        with open(FILE_DOCTORS, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["DoctorName", "Specialty", "TimeSlot", "PasswordHash"])
            
    if not os.path.exists(FILE_PATIENTS) or os.stat(FILE_PATIENTS).st_size == 0:
        with open(FILE_PATIENTS, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["PatientName", "PasswordHash"])

    if not os.path.exists(FILE_APPTS) or os.stat(FILE_APPTS).st_size == 0:
        with open(FILE_APPTS, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ApptID", "PatientName", "DoctorName", "Status"])

# --- Core Classes ---
class Doctor:
    def __init__(self):
        self.name = ""
        self.is_logged_in = False

    def register(self):
        speak("Let's set up your doctor profile.")
        name = get_hybrid_input("Please say your full name.")
        specialty = get_hybrid_input("What is your medical specialty?")
        time_slot = get_hybrid_input("Say your clinic timings. For example, 10 AM to 2 PM.")
        
        raw_password = str(random.randint(1000, 9999))
        hashed_pw = hash_password(raw_password)
        
        with open(FILE_DOCTORS, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([name, specialty, time_slot, hashed_pw])
            
        speak(f"Registration successful. Doctor {name}, please write down your 4 digit login password. It is {raw_password}.")

    def login(self):
        name = get_hybrid_input("Doctor Login. Please say your registered name.")
        password = get_hybrid_input("Please say or type your 4 digit password.")
        hashed_input = hash_password(password)

        try:
            with open(FILE_DOCTORS, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if len(row) >= 4 and row[0].lower() == name.lower() and row[3] == hashed_input:
                        self.name = row[0]
                        self.is_logged_in = True
                        speak(f"Login successful. Welcome back, Doctor {self.name}.")
                        return True
        except FileNotFoundError:
            pass

        speak("Login failed. I could not match that name and password.")
        return False

    def manage_appointments(self):
        if not self.is_logged_in:
            return

        appointments = []
        try:
            with open(FILE_APPTS, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)
                appointments = list(reader)
        except FileNotFoundError:
            pass

        pending_apps = []
        for row in appointments:
            if len(row) >= 4 and row[2].lower() == self.name.lower() and row[3] == "Pending":
                pending_apps.append(row)

        if not pending_apps:
            speak("You have no pending appointment requests at this time.")
            return

        speak(f"You have {len(pending_apps)} pending requests. I will read them now.")
        
        valid_ids = []
        for appt in pending_apps:
            valid_ids.append(appt[0].lower())
            speak(f"Appointment ID {appt[0]}. Requested by patient {appt[1]}.")

        choice = get_hybrid_input("Please say the Appointment ID you want to process, or say cancel.")
        
        if choice.lower() in valid_ids:
            target_id = next(id for id in valid_ids if id == choice.lower())
            
            action = get_hybrid_input("Do you want to Approve or Reject this appointment?")
            new_status = "Approved" if "approve" in action.lower() else "Rejected"
            
            for row in appointments:
                if row[0].lower() == target_id:
                    row[3] = new_status
                    
            with open(FILE_APPTS, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if header: writer.writerow(header)
                writer.writerows(appointments)
                
            speak(f"Success. Appointment {choice} has been {new_status}.")
        else:
            speak("Action cancelled. Returning to main menu.")


class Patient:
    def __init__(self):
        self.name = ""
        self.is_logged_in = False

    def register(self):
        speak("Let's create your patient account.")
        name = get_hybrid_input("Please say your full name.")
        
        raw_password = str(random.randint(1000, 9999))
        hashed_pw = hash_password(raw_password)
        
        with open(FILE_PATIENTS, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([name, hashed_pw])
            
        speak(f"Registration successful. Hello {name}, please write down your 4 digit login password. It is {raw_password}.")

    def login(self):
        name = get_hybrid_input("Patient Login. Please say your registered name.")
        password = get_hybrid_input("Please say or type your 4 digit password.")
        hashed_input = hash_password(password)

        try:
            with open(FILE_PATIENTS, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if len(row) >= 2 and row[0].lower() == name.lower() and row[1] == hashed_input:
                        self.name = row[0]
                        self.is_logged_in = True
                        speak(f"Login successful. Welcome, {self.name}.")
                        return True
        except FileNotFoundError:
            pass

        speak("Login failed. I could not match that name and password.")
        return False

    def dashboard(self):
        if not self.is_logged_in: return
        
        while True:
            action = get_hybrid_input("Patient Dashboard. Do you want to book an appointment, check your status, or log out?")
            action_lower = action.lower()
            
            if 'book' in action_lower:
                self.book_appointment()
            elif 'check' in action_lower or 'status' in action_lower:
                self.check_status()
            elif 'out' in action_lower or 'exit' in action_lower:
                speak("Logging you out now.")
                break
            else:
                speak("I did not understand that choice.")

    def book_appointment(self):
        doctors_available = []
        try:
            with open(FILE_DOCTORS, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None) 
                for row in reader:
                    if len(row) >= 3:
                        doctors_available.append(row)
        except FileNotFoundError:
            speak("There is a database error. Please try again later.")
            return

        if not doctors_available:
            speak("There are currently no doctors registered in the system.")
            return

        speak("I will now read the list of available doctors.")
        valid_doctor_names = []
        
        for doc in doctors_available:
            valid_doctor_names.append(doc[0].lower())
            speak(f"Doctor {doc[0]}. Specialty is {doc[1]}. Available from {doc[2]}.")
        
        doctor_choice = get_hybrid_input("Please say the name of the doctor you would like to visit.")
        
        if doctor_choice.lower() in valid_doctor_names:
            target_doc = next(name for name in valid_doctor_names if name == doctor_choice.lower())
            
            appt_id = "APT" + str(random.randint(100, 999))
            with open(FILE_APPTS, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([appt_id, self.name, target_doc, "Pending"])
                
            speak(f"Success. Your appointment with Doctor {doctor_choice} has been requested. Your ID is {appt_id}.")
        else:
            speak("I could not find a doctor with that name. Returning to dashboard.")

    def check_status(self):
        found_appointments = False
        try:
            with open(FILE_APPTS, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader, None)
                for row in reader:
                    if len(row) >= 4 and row[1].lower() == self.name.lower():
                        if not found_appointments:
                            speak("Here are your current appointments.")
                            found_appointments = True
                        
                        speak(f"Appointment ID {row[0]} with Doctor {row[2]}. Status is: {row[3]}.")
        except FileNotFoundError:
            pass

        if not found_appointments:
            speak("You currently have no appointment records in the system.")

# --- Main Execution ---
def main():
    init_db()
    speak("System starting. Welcome to the Smart Clinic Audio Portal.")

    while True:
        choice = get_hybrid_input("Main Menu. Please say 'One' for Doctor Portal. 'Two' for Patient Portal. Or 'Three' to shut down.")
        choice_lower = choice.lower()
        
        if '1' in choice_lower or 'one' in choice_lower or 'doctor' in choice_lower:
            doc = Doctor()
            action = get_hybrid_input("Doctor Portal. Do you want to Login, or Register a new account?")
            if 'register' in action.lower():
                doc.register()
            elif 'login' in action.lower():
                if doc.login():
                    doc.manage_appointments()
                    
        elif '2' in choice_lower or 'two' in choice_lower or 'patient' in choice_lower:
            pat = Patient()
            action = get_hybrid_input("Patient Portal. Do you want to Login, or Register a new account?")
            if 'register' in action.lower():
                pat.register()
            elif 'login' in action.lower():
                if pat.login():
                    pat.dashboard()
                    
        elif '3' in choice_lower or 'three' in choice_lower or 'shut' in choice_lower or 'exit' in choice_lower:
            speak("Shutting down the Smart Clinic. Goodbye.")
            break
        else:
            speak("I did not understand. Please try again.")

if __name__ == "__main__":
    try:
        print("\n=== SMART CLINIC TERMINAL RUNNING ===")
        print("Note: The system is running in Audio-Parity Mode for accessibility.")
        main()
    except KeyboardInterrupt:
        speak("System forcefully closed. Goodbye.")
        print("\n\n🛑 System forcefully exited by user.")