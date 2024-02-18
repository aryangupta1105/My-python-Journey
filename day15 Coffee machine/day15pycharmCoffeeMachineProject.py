from menu import MENU
def display_report():
    return f"Water: {Total_water} \nMilk: {Total_milk}\nCoffee: {Total_Coffee}\nMoney: {round(Total_Money,2)}"

def check_transaction(coffee , put_money):
    cost = coffee['cost']
    if put_money >= cost:
        return True
    else:
        return False

def resource_checker(coffee):
    milk = coffee['ingredients']['milk']
    water = coffee['ingredients']['water']
    coffee = coffee['ingredients']['coffee']
    if Total_Coffee < coffee:
        print("Insufficient coffee")
        return False
    elif Total_water < water:
        print("Insufficient water")
        return False
    elif Total_milk < milk:
        print("Insufficient milk")
        return False
    else:
        return True


    
def deposit_money(coffee):
    
    amount_quarters = float(int(input("How many quarters?: "))*0.25)
    amount_pennies = float(int(input("How many pennies?: ")) * 0.01)
    amount_nickles = float(int(input("How many nickels?: ")) * 0.05)
    amount_dimes = float(int(input("How many dimes?: ")) * 0.10)


    Total_deposit = amount_dimes+ amount_nickles+amount_pennies + amount_quarters

    return Total_deposit

def resource_updater(chosen_coffee):
    global Total_milk, Total_water, Total_Coffee, Total_Money
    Total_milk = Total_milk - chosen_coffee['ingredients']['milk']
    Total_water = Total_water - chosen_coffee['ingredients']['water']
    Total_Coffee = Total_Coffee - chosen_coffee['ingredients']['coffee']
    Total_Money += chosen_coffee['cost']


def make_coffee(chosen_coffee):
    if resource_checker(chosen_coffee):
        deposited_money = deposit_money(chosen_coffee)
        print(f"Deposited money {deposited_money}")
        if check_transaction(chosen_coffee, deposited_money):
            change = deposited_money - chosen_coffee['cost'] 
            print(f"here's your change: {change}")
            resource_updater(chosen_coffee)
            print(f"Enjoy your coffee..!")
        else:
            print("Transaction failed! Insufficient money...")

def coffee_machine():
    global Total_milk, Total_water, Total_Coffee, Total_Money
    Total_milk = 300
    Total_water = 200
    Total_Coffee = 100
    Total_Money = 0
    keep_running = True
    while keep_running:
        ask = input("What would you like? 'espresso', 'latte', 'cappuccino', or 'report' to get a report, or 'cancel' to cancel:\nEnter: ").lower()
        if ask == 'espresso' or ask == 'latte' or ask == 'cappuccino':
            make_coffee(MENU[ask])
        elif ask == 'report':
            print(display_report())
        elif ask == 'cancel':
            keep_running = False
        else:
            print("Invalid input. Please enter 'espresso', 'latte', 'cappuccino', 'report', or 'cancel'.")

coffee_machine()
        
        