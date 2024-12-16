import json

def is_password_strong(password):
    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return False
    if password.isdigit() or password.isalpha():
        print("Password must contain both letters and numbers for security.")
        return False
    return True

def display_menu():
    print("\nUser Management System")
    print("1. Add User")
    print("2. Remove User")
    print("3. Change Username")
    print("4. Change Password")
    print("5. Display Users")
    print("6. Show Password by Login")
    print("7. Load Users from File")
    print("8. Save Users to File")
    print("0. Exit")

def save_users(users, filename="users.txt"):
    try:
        with open(filename, "w") as file:
            json.dump(users, file)
        print(f"Users saved successfully to '{filename}'.")
    except Exception as e:
        print(f"Error saving users: {e}")

def load_users(filename="users.txt"):
    try:
        with open(filename, "r") as file:
            users = json.load(file)
        print(f"Users loaded successfully from '{filename}'.")
        return users
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty user list.")
        return {}
    except Exception as e:
        print(f"Error loading users: {e}")
        return {}

def main():
    users = {}
    
    while True:
        display_menu()
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            login = input("Enter new login: ")
            
            if login in users:
                print("Login already exists.")
                continue
            password = input("Enter new password: ")

            if not is_password_strong(password):
                print("Incorrect password. Remake it!")
                continue
            
            users[login] = password
            print(f"User '{login}' added successfully.")
        
        elif choice == "2":
            login = input("Enter login to remove: ")
            
            if login not in users:
                print("Login does not exist.")
                continue
            
            del users[login]
            print(f"User '{login}' removed successfully.")
        
        elif choice == "3":
            old_login = input("Enter current login: ")
            
            if old_login not in users:
                print("Login does not exist.")
                continue
            
            new_login = input("Enter new login: ")
            
            if new_login in users:
                print("New login already exists.")
                continue
            
            users[new_login] = users.pop(old_login)
            print(f"Login changed from '{old_login}' to '{new_login}'.")
        
        elif choice == "4":
            login = input("Enter login to change password: ")
            
            if login not in users:
                print("Login does not exist.")
                continue
            
            new_password = input("Enter new password: ")
            
            if new_password == users[login]:
                print("New password cannot be the same as the old password.")
                continue
            
            if not is_password_strong(new_password):
                print("Incorrect password. Remake it!")
                continue
            
            users[login] = new_password
            print("Password updated successfully.")
        
        elif choice == "5":
            print("\nCurrent Users:")
            for login, password in users.items():
                print(f"Login: {login}")
        
        elif choice == "6":
            login = input("Enter login to display password: ")
            
            if login not in users:
                print("Login does not exist.")
                continue
            
            print(f"The password for '{login}' is: {users[login]}")
        
        elif choice == "7":
            users = load_users()
        
        elif choice == "8":
            save_users(users)
        
        elif choice == "0":
            print("Exiting program.")
            break
        
        else:
            print("Invalid option. Please try again.")

main()
