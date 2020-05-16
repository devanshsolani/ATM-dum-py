print("Welcome to the Desol ATM")
restart = ("Y")
pin = int(input("Please set your pin number: "))

chances = 3
balance = int(input("How much balance do you wish in your dummy A/C? "))
while chances >=0:
    pin = int(input("Please enter your 4 Digit Pin: "))
    if pin == pin:
        while restart not in ('n', 'NO', 'no', 'N'):
            print("You entered your pin correctly")
            print("Please press 1 for your Balance Check, \n 2 to Make a Withdrawal, \n 3 To Pay_In. ")
            option = int(input("What would you like to choose?: "))
            if option == 1:
                print("Your balance is ",balance)
                restart = input("Would you like to go back? Type yes. ")
                if restart in ('n', 'NO', 'no', 'N'):
                    print("Thank you!")
                    break

            elif option == 2:
                withdrawal = float(input("How much amount would you like to withdraw? "))
                if balance>withdrawal:
                    balance=balance-withdrawal
                    print("Now your balance is", balance)
                else:
                    print("You have only RS ", balance)
                    restart = input("Would you like to go back? Type yes. ")
                    if restart in ('n', 'NO', 'no', 'N'):
                        print("Thank you!")
                        break
            elif option==3:
                pay_in = float(input("How much would you like to PAY_IN? "))
                print("Please wait while we process your request")
                balance = pay_in + balance
                print("Now your balance is", balance)
                print("Please wait while we return your Credit Card...")
                break
            else:
                print("Please enter a valid number. \n")
                restart=('y')

    elif pin != pin:
        print("Incorrect Password")
        chances = chances-1
        if chances == 0:
            print("Your card is blocked. No more tries available.\n Contact the local bank authority to unblock your card for further convenience.")
            break