from art import text2art
from colorama import Fore, Style, init
from bloodBank import BloodBank

# Initialize Colorama
init(autoreset=True)

def display_menu():
    print(Fore.RED + text2art("Blood Bank", font='sub-zero'))
    print(Fore.GREEN + "Welcome to our Blood Bank Management System, where every drop counts!")
    print(Fore.YELLOW + "1. Add Donor")
    print(Fore.YELLOW + "2. View Donors")
    print(Fore.YELLOW + "3. Search Donor")
    print(Fore.YELLOW + "4. Total Blood Quantity")
    print(Fore.YELLOW + "5. Exit")

def main():
    blood_bank = BloodBank()
    while True:
        display_menu()
        choice = input(Fore.CYAN + "Choose an option (1-5): ")

        try:
            if choice == '1':
                name = input(Fore.CYAN + "Enter donor name: ")
                age = int(input(Fore.CYAN + "Enter donor age: "))
                gender = input(Fore.CYAN + "Enter donor gender (M/F/Other): ")
                email = input(Fore.CYAN + "Enter donor email address: ")
                phone = input(Fore.CYAN + "Enter donor phone number: ")
                blood_type = input(Fore.CYAN + "Enter blood type (A, B, AB, O): ")
                quantity = float(input(Fore.CYAN + "Enter quantity of blood (in liters): "))
                blood_bank.add_donor(name, age, gender, email, phone, blood_type, quantity)
            elif choice == '2':
                blood_bank.view_donors()
            elif choice == '3':
                donor_id = int(input(Fore.CYAN + "Enter donor ID to search: "))
                blood_bank.search_donor(donor_id)
            elif choice == '4':
                total_quantity = blood_bank.total_blood_quantity()
                print(Fore.GREEN + f"Total blood quantity in the bank: {total_quantity} liters")
            elif choice == '5':
                print(Fore.RED + "Exiting the system.")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")
        except ValueError as ve:
            print(Fore.RED + f"Input error: {ve}")
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()