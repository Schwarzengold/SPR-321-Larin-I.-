class TemperatureConverter:
    countconv = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.countconv += 1
        return celsius * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.countconv += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.countconv

def print_menu():
    print("=" * 40)
    print("          Temperature Converter")
    print("=" * 40)
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Show conversion count")
    print("4. Exit")
    print("=" * 40)

def main():
    while True:
        print_menu()
        
        choice = input("Enter your choice: ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
            
            print(f"\nYour temperature {celsius}°C is {fahrenheit:.2f}°F\n")
            
        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
            
            print(f"\nYour temperature {fahrenheit}°F is {celsius:.2f}°C\n")
            
        elif choice == "3":
            count = TemperatureConverter.get_conversion_count()
            
            print(f"\nTotal conversions made: {count}\n")
            
        elif choice == "4":
            
            print("\n-==<< Have a nice day! :) >>==-\n")
            exit()
            
        else:
            print("\n -==<< Invalid choice. Please try again >>==- \n")

main()
