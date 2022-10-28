from cunstomer_account import CustomerAccount

# Creating an instance of the customer account
cust1 = CustomerAccount()


def welcome_screen():
    print('***Welcome to Ecobank Auto System***')
    user_input = int(input('1. Show Balance\n'
                           '2. Withdraw\n'
                           '3. Deposit\n'
                           '4. Cancel\n\n'
                           'Provide Request : '))
    user_options(user_input)


def user_options(user_input):
    if user_input == 1:
        show_user_balance()
    elif user_input == 2:
        user_withdraw()
    elif user_input == 3:
        user_deposit()
    elif user_input == 4:
        user_cancel()
    else:
        print('Invalid request, try again!')
    welcome_screen()


def show_user_balance():
    print(f'Your account balance is : GHC {cust1.check_balance()}')


def user_deposit():
    amount = float(input('Enter amount : '))
    if amount > 0:
        cust1.deposit(amount)
        print(f'GHC{amount} deposited successfully.')
    else:
        print('Invalid amount provided, try again.')


def user_withdraw():
    amount = float(input('Enter amount to redraw : '))
    if amount > 0:
        if not amount > cust1.check_balance():
            cust1.withdraw(amount)
            print(f'GHC {amount} has been withdrawn successfully.')
        else:
            print('Not eligible to withdraw the amount entered!')

    else:
        print('Invalid amount to withdraw, try again.')


def user_cancel():
    print('Thanks for using our services. Hope to see you again!')
    exit()
    pass


welcome_screen()
