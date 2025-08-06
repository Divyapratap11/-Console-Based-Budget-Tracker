from budget_tracker import BudgetTracker

def main():
    tracker = BudgetTracker()

    while True:
        print("\n--- Budget Tracker Menu ---")
        print("1. Add a Transaction")
        print("2. List All Transactions")
        print("3. Filter Transactions")
        print("4. View Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                t_type = input("Enter type (income/expense): ").lower()
                if t_type not in ["income", "expense"]:
                    print("Invalid type!")
                    continue
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                notes = input("Enter notes (optional): ")
                tracker.add_transaction(amount, category, t_type, notes)
                print("Transaction added successfully.")
            except ValueError:
                print("Invalid input! Please enter numeric values for amount.")

        elif choice == "2":
            tracker.list_transactions()

        elif choice == "3":
            f_type = input("Filter by type (income/expense or leave blank): ").lower()
            f_cat = input("Filter by category (or leave blank): ")
            tracker.filter_transactions(by_type=f_type if f_type else None,
                                        by_category=f_cat if f_cat else None)

        elif choice == "4":
            tracker.view_summary()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()