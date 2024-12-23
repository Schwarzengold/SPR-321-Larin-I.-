class Airplane:
    TYPE_LIMITS = {1:("Private", 20), 2:("Medium", 50), 3:("Airliner", 300)}

    def __init__(self, name, plane_type):
        if plane_type not in Airplane.TYPE_LIMITS:
            raise ValueError("\n -==<< Invalid plane type. Choose a valid number >>==-\n")
        self.name = name
        self.plane_type = Airplane.TYPE_LIMITS[plane_type][0]
        self.passengers = 0

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("\n -==<< Can only add a positive integer >>==-\n")
        if self.passengers + num > Airplane.TYPE_LIMITS[self._get_type_key()][1]:
            raise ValueError("\n -==<< Exceeds maximum capacity! Try again >>==-\n")
        self.passengers += num
        return self

    def __sub__(self, num):
        if not isinstance(num, int) or num <= 0:
            raise ValueError("\n -==<< Can only subtract a positive integer >>==- \n")
        if self.passengers - num < 0:
            raise ValueError("\n -==<< Cannot have negative passengers >>==- \n")
        self.passengers -= num
        return self

    def __iadd__(self, num):
        return self + num

    def __isub__(self, num):
        return self - num

    def __gt__(self, other):
        return self.passengers > other.passengers

    def __lt__(self, other):
        return self.passengers < other.passengers

    def __ge__(self, other):
        return self.passengers >= other.passengers

    def __le__(self, other):
        return self.passengers <= other.passengers

    def __int__(self):
        return self.passengers

    def __str__(self):
        return self.plane_type

    def _get_type_key(self):
        for key, (ptype, _) in Airplane.TYPE_LIMITS.items():
            if ptype == self.plane_type:
                return key

def print_menu():
    print("=" * 70)
    print("\t\t     Airplane Management System")
    print("=" * 70)
    print("1. Add airplanes")
    print("2. Manage passengers")
    print("3. Compare airplanes")
    print("4. Exit")
    print("=" * 70)

def add_airplanes():
    def get_plane_type():
        print("\nChoose a type:\n")
        for key, (ptype, capacity) in Airplane.TYPE_LIMITS.items():
            print(f"{ptype} (max capacity {capacity}) - {key}")
        while True:
            try:
                plane_type = int(input("\n<< Enter the number corresponding to the type >> : "))
                if plane_type in Airplane.TYPE_LIMITS:
                    return plane_type
                else:
                    print("\n-==<< Invalid choice. Please enter 1, 2, or 3. >>=- ")
            except ValueError:
                print("\n-==<< Invalid input. Please enter a number >>==-\n")

    name1 = input("\n<< Enter the name of the first airplane >> : ")
    type1 = get_plane_type()
    airplane1 = Airplane(name1, type1)

    name2 = input("\n<< Enter the name of the second airplane >>: ")
    type2 = get_plane_type()
    airplane2 = Airplane(name2, type2)

    return airplane1, airplane2

def manage_passengers(airplane):
    while True:
        print("=" * 70)
        print(f"Managing passengers for {airplane.name}")
        print("=" * 70)
        print("1. Add passengers")
        print("2. Remove passengers")
        print("3. Add one passenger")
        print("4. Remove one passenger")
        print("5. Back")
        print("=" * 70)
        choice = input("<< Enter your choice >>: ")

        if choice == "1":
            try:
                num = int(input("\n<< How many passengers to add? >> : "))
                airplane += num
                print(f"\n-==<< {num} passengers added. Current count: {airplane.passengers} >>==-\n")
            except ValueError as e:
                print(e)
        elif choice == "2":
            try:
                num = int(input("\n How many passengers to remove? "))
                airplane -= num
                print(f"\n-==<< {num} passengers removed. Current count: {airplane.passengers} >>==-\n")
            except ValueError as e:
                print(e)
        elif choice == "3":
            try:
                airplane += 1
                print(f"\n-==<< One passenger added. Current count: {airplane.passengers} >>==-\n")
            except ValueError as e:
                print(e)
        elif choice == "4":
            try:
                airplane -= 1
                print(f"\n-==<< One passenger removed. Current count: {airplane.passengers} >>==-\n")
            except ValueError as e:
                print(e)
        elif choice == "5":
            break
        else:
            print("\n -==<< Invalid choice. Try again >>==- \n")

def compare_airplanes(airplane1, airplane2):
    print("=" * 70)
    print("Comparing airplanes:")
    print("=" * 70)
    if airplane1 > airplane2:
        print(f"{airplane1.name} has more passengers ({airplane1.passengers}) than {airplane2.name} ({airplane2.passengers}).")
    elif airplane1 < airplane2:
        print(f"{airplane2.name} has more passengers ({airplane2.passengers}) than {airplane1.name} ({airplane1.passengers}).")
    else:
        print(f"Both airplanes have the same number of passengers ({airplane1.passengers}).")

    if airplane1 == airplane2:
        print(f"Both airplanes are of the same type: {airplane1.plane_type}.")
    else:
        print(f"\nThe airplanes are of different types: {airplane1.plane_type} and {airplane2.plane_type}.")

def main():
    airplane1, airplane2 = None, None

    while True:
        print_menu()
        choice = input("<< Enter your choice >> : ")

        if choice == "1":
            try:
                airplane1, airplane2 = add_airplanes()
                print("\n -==<< Airplanes added successfully! >>==- \n")
            except ValueError as e:
                print(e)
        elif choice == "2":
            if not airplane1 or not airplane2:
                print("\n -==<< Please add airplanes first >>==- \n")
                continue
            print("=" * 70)
            print("1. Manage 1 airplane")
            print("2. Manage 2 airplane")
            print("=" * 70)
            sub_choice = input("<< Choose airplane >> : ")

            if sub_choice == "1":
                manage_passengers(airplane1)
            elif sub_choice == "2":
                manage_passengers(airplane2)
            else:
                print("\n -==<< Invalid choice. Try again >>==- \n")
        elif choice == "3":
            if not airplane1 or not airplane2:
                print("\n -==<< Please add airplanes first >>==-\n")
                continue
            compare_airplanes(airplane1, airplane2)
        elif choice == "4":
            print("\n-==<< Have a nice day :) >>==-\n")
            exit()
        else:
            print("\n -==<< Invalid choice. Try again >>==- \n")

main()
