class Passport:
    def __init__(self):
        self.full_name = None
        self.date_of_birth = None
        self.place_of_birth = None
        self.passport_id = None

    def add_info(self):
        self.full_name = input("Enter full name: ")
        self.date_of_birth = input("Enter date of birth (DD-MM-YYYY): ")
        self.place_of_birth = input("Enter place of birth: ")
        self.passport_id = input("Enter passport ID: ")

    def __str__(self):
        return ("=========================================\n"f"Passport Info:\n\n"f"Full Name: {self.full_name}\n"f"Date of Birth: {self.date_of_birth}\n"f"Place of Birth: {self.place_of_birth}\n"f"Passport ID: {self.passport_id}")

class ForeignPassport(Passport):
    def __init__(self):
        super().__init__()
        self.foreign_passport_id = None
        self.visas = []

    def add_foreign_info(self):
        self.foreign_passport_id = input("Enter foreign passport ID: ")

    def add_visa(self):
        visa_number = input("Enter visa number: ")
        if visa_number not in self.visas:
            self.visas.append(visa_number)
            print("\nVisa added successfully!")
        else:
            print("\nThis visa number already exists!")

    def remove_visa(self):
        visa_number = input("Enter the visa number to remove: ")
        if visa_number in self.visas:
            self.visas.remove(visa_number)
            print("\nVisa removed successfully!")
        else:
            print("\nVisa not found!")

    def __str__(self):
        passport_info = super().__str__()
        if self.visas:
            visas_info = ", ".join(self.visas)
        else:
            visas_info = "No visas"

        return (f"{passport_info}\n"f"Foreign Passport ID: {self.foreign_passport_id}\n"f"Visas: {visas_info}")

foreign_passport = ForeignPassport()

while True:
    print("=========================================")
    print("                 Menu:")
    print("=========================================")
    print("1. Add passport info")
    print("2. Add foreign passport info")
    print("3. Add visa")
    print("4. Remove visa")
    print("5. Display passport info")
    print("6. Exit")
    print("=========================================")
    choice = input("Choose an option: ")

    if choice == "1":
        foreign_passport.add_info()
    elif choice == "2":
        foreign_passport.add_foreign_info()
    elif choice == "3":
        foreign_passport.add_visa()
    elif choice == "4":
        foreign_passport.remove_visa()
    elif choice == "5":
        print(f"\n{foreign_passport}")
    elif choice == "6":
        print(" -==<< Goodbye! >>==- ")
        exit()
    else:
        print("-==<< Invalid choice! Please try again. >>==- ")
