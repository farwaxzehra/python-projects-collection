accounts = []

def create_acc():
    acc_name = input('Enter username: ')
    acc_no = int(input('Enter Account Number: '))
    initial_bal = int(input('Enter initial deposit: '))

    account = {'Account Name': acc_name, 
               'Account Number': acc_no,
               'Balance': initial_bal}

    accounts.append(account)
    print(f'Account Created! Hello, {acc_name}.')


def deposit():
    acc_no = int(input('Enter your account number: '))

    for acc in accounts:
        if acc_no == acc['Account Number']:
            deposit_am = int(input('Enter amount to deposit: '))
            acc['Balance'] += deposit_am
            print('You have deposited your amount successfully!')
            return

    print('Account not Found!')


def withdraw():
    acc_no = int(input('Enter your account number: '))

    for acc in accounts:
        if acc_no == acc['Account Number']:
            withdrawal_am = int(input('Enter your withdrawal amount: '))
            if acc['Balance'] >= withdrawal_am:
                acc['Balance'] -= withdrawal_am
                print('Withdraw successful!')
            else:
                print('Insufficient balance.')
            return

    print('Account not Found!')


def check():
    acc_no = int(input('Enter your Account number: '))

    for acc in accounts:
        if acc_no == acc['Account Number']:
            print("Account Name:", acc["Account Name"])
            print("Current Balance:", acc["Balance"])
            return

    print('Account not found')


while True:
    print('Banking System'.center(70))
    print('1. Create Account')
    print('2. Deposit Money')
    print('3. Withdraw money')
    print('4. Check Balance')
    print('5. Exit program')
    
    ch = input('Choose your option (1-5): ')
    
    if ch == '1':
        create_acc()
    elif ch == '2':
        deposit()
    elif ch == '3':
        withdraw()
    elif ch == '4':
        check()
    elif ch == '5':
        print('Exiting Program. Thank you')
        break
    else:
        print('Please, enter valid choice')