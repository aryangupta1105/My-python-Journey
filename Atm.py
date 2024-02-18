import random
print("Welcome to Python Payments Bank ATM")
card_list = ['5820 4325 2356','5720 4328 5703','3282 4435 2317']
for card in card_list:
    print(card)
Pin = 1739
balance_list = [2242,22,3424 ,344, 3291, 4354,324, 245, 53233, 234342, 23456, 84, 34563]
balance = random.choice(balance_list)

def Withdrawal(balance):
    cash_option = int(input("Type '1' for Fast Cash withdrawal , '2' for custom cash withdrawal\n"))
    if cash_option == 1:
        fast_cash = int(input("Choose:\n1)500rs\n2)1000rs\n3)2000rs\n4)5000rs"))
        for digits in range(0,4):
            display += "_"
        print(display)
        entered_pin = int(input("Enter the Four digit pin:"))
        if entered_pin == Pin:
            if fast_cash ==1:
                amount = 500
                if amount<balance:
                    balance -= amount
                    print(f"500rs Withdrawed!")
                else:
                    print("Insufficient Balance!")
            elif fast_cash ==2:
                amount = 1000
                if amount<balance:
                    balance -= amount
                    print(f"1000rs Withdrawed!")
                else:
                    print("Insufficient Balance!")
            elif fast_cash ==3:
                amount = 2000
                if amount<balance:
                    balance -= amount
                    print(f"2000rs Withdrawed!")
                else:
                    print("Insufficient Balance!")
            elif fast_cash ==4:
                amount = 5000
                if amount< balance:
                    balance -= amount
                    print(f"5000rs Withdrawed!")
                else:
                    print("Insufficient Balance!")
            else:
                print("Invalid Card Number!!")
        else:
            print("Invalid Pin!! Transaction cancelled....")
    elif cash_option == 2:
        amount = int(input("Enter the amount:-  Rs"))
        if balance > amount:
            balance -= amount
            print(f"{amount} Withdrawed! and {balance}rs left. ")
        else:
            print(f"Your balance is {balance}.\nInsufficient Balance!!")
    else:
        print("Error!!")

def Balance_check(balance,Pin):
    entered_pin = int(input("Enter the Four digit pin:"))
    if entered_pin == Pin:
        print(balance)
    else:
        print("Invalid Pin!!")


card_inserted = input("Enter Your Card Number:- ")
for cards in card_list:
    if card_inserted == cards:
        options = input("Choose: 1 for Cash Withdrawal \n2 for Balance enquiry\n3 for Generate/reset Pin:\n")
        if options == '1':
            Withdrawal(balance,Pin)
        elif options == '2':
            Balance_check(balance,Pin)
        elif options == '3':
            Green_pin(balance,Pin)
        else:
            print("Invalid option!! Transaction Cancelled....")
    else:
        print("Invalid Card Number!!")



