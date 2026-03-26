import random

def generate_pin():
    # Generate a random 4-digit PIN as a string with leading zeros if needed
    pin = f"{random.randint(0, 9999):04d}"
    return pin

def main():
    print("Select an option:")
    print("1. Generate a 4-digit PIN")
    print("2. Exit")

    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == '1':
            pin = generate_pin()
            print(f"Generated 4-digit PIN: {pin}")
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
