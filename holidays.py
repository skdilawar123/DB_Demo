from employee import update_holiday

Holidays = {}

def Holidays_managemnt():
    print("Select an option")
    print("1. Add holiday")
    print("2. Update holiday")
    print("3. View all holidays")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = Holidays_managemnt()
        if choice == '1':
            add_holidays()
        elif choice == '2':
            update_holidays()
        elif choice == '3':
            view_holidays()
        else:
            print("Invalid option")

def add_holidays():
    holiday_name = input("Enter name of the holiday: ")
    holiday_id = len(Holidays) + 1  # Generate a unique ID based on current length of the dict
    Holidays[holiday_id] = {'name': holiday_name}
    holiday_date = input("Enter the date of the holiday (DDMMYYYY): ")
    Holidays[holiday_id]['date'] = holiday_date
    print(f"Your holiday '{holiday_name}' added successfully")

def update_holidays():
    holiday_id = int(input("Enter the holiday ID to update holiday: "))
    if holiday_id in Holidays:
        new_name = input("Enter the new holiday name: ")
        new_date = input("Enter the new date: ")
        Holidays[holiday_id]['name'] = new_name
        Holidays[holiday_id]['date'] = new_date
        print(f"Your holiday '{new_name}' with date {new_date} is updated successfully")
    else:
        print("Holiday ID not found.")

def view_holidays():
    if Holidays:
        print("All holidays:")
        for holiday_id, holiday_info in Holidays.items():
            print(f"Holiday ID: {holiday_id}, Name: {holiday_info['name']}, Date: {holiday_info['date']}")
    else:
        print("No holidays added yet.")

main()
