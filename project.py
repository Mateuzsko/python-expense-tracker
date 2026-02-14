def add_expense(amount, category):
    with open("expenses.txt", "a") as file:
        file.write(f"{amount}, {category}\n")

def show_expenses():
    try:
       with open("expenses.txt", "r") as file:
        print("\n--- Expenses ---")
        for line in file:
            amount, category = line.strip().split(",")
            print(f"{category}: ${amount}")
    except FileNotFoundError:
        print("No expenses yet")


while True:
    print("\n1. Add expeense ")
    print("2. Show expenses ")
    print("3. Exit ")

    choice = input("Choose an option ")

    if choice == "1":
        try:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(amount, category)
            print("Expense added!")
        except ValueError:
                print("invalid number.")
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice.")