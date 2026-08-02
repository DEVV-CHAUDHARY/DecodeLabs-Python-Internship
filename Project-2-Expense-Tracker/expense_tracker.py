def display_menu():
    print("\n" + "=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Total")
    print("3. Exit")
    print("=" * 40)


def main():
    total = 0

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                expense = float(input("Enter Expense Amount: ₹"))
                total += expense
                print(f"✅ Expense of ₹{expense:.2f} added successfully.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "2":
            print(f"\n💰 Total Expense = ₹{total:.2f}")

        elif choice == "3":
            print("\nThank you for using Expense Tracker.")
            break

        else:
            print("❌ Invalid Choice")


if __name__ == "__main__":
    main()