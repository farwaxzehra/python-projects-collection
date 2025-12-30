# %% 
users = []  
login_attempts = []  

while True:
    print("\nMini Cloud Security Monitor")
    print("1. Login / Register")
    print("2. View User Summary")
    print("3. Exit")
    
    try:
        ch = int(input("Select your choice: "))
    except ValueError:
        print("Enter a valid number")
        continue


    if ch == 1:
        username = input("Enter Username: ")
        try:
            pin = int(input("Enter PIN: "))
        except ValueError:
            print("PIN must be numeric")
            continue

        found = False
        for user in users:
            if user['Username'] == username:
                found = True
                if user['Pin'] == pin:
                    print("Login Success ")
                    login_attempts.append({'Username': username, 'Status': 'Success'})
                else:
                    print("Wrong PIN")
                    login_attempts.append({'Username': username, 'Status': 'Failed'})
                break

        if not found:
            users.append({'Username': username, 'Pin': pin})
            print("User registered successfully ")
            login_attempts.append({'Username': username, 'Status': 'Registered'})

    elif ch == 2:
        if not login_attempts:
            print("No login attempts yet.")
        else:
            summary = {}
            for attempt in login_attempts:
                user = attempt['Username']
                status = attempt['Status']
                if user not in summary:
                    summary[user] = {'Success': 0, 'Failed': 0, 'Registered': 0}
                if status == 'Success':
                    summary[user]['Success'] += 1
                elif status == 'Failed':
                    summary[user]['Failed'] += 1
                elif status == 'Registered':
                    summary[user]['Registered'] += 1

            print("\nUser Summary:")
            for user, stats in summary.items():
                print(f"{user} -> Registered: {stats['Registered']}, Success: {stats['Success']}, Failed: {stats['Failed']}")

    elif ch == 3:
        print("Exiting program. Goodbye! 👋")
        break

    else:
        print("Invalid choice. Enter 1-3.")