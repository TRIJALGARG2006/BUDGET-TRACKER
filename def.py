def budget_tracker():
    balance = int(input("enter balance :"))
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Balance")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                if amount > 0:
                    balance += amount
                    print(f"New Balance: ${balance:.2f}")
                else:
                    print("Error: Amount must be positive.")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
                break

        elif choice == '2':
            try:
                amount = float(input("Enter amount: "))
                if amount <= 0:
                    print("Error: Amount must be positive.")
                elif amount > balance:
                    print("Error: Insufficient funds.")
                else:
                    balance -= amount
                    print(f"New Balance: ${balance:.2f}")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
                break

        elif choice == '3':
            print(f"Current Balance: ${balance:.2f}")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3")

budget_tracker()
