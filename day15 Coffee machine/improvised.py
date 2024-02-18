from menu import MENU

resources = {
    'milk' :300,
    "water": 200,
    'coffee': 100,
}
Total_Money = 0

def display_report():
    print(f"Water: {resources['water']} \nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {round(Total_Money,2)}")


def check_transaction(coffee , put_money):
    cost = coffee['cost']
    if put_money >= cost:
        return True
    else:
        return False

def resource_checker(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Insufficient {item}")
            return False
    return True

    
def deposit_money(coffee):
    amount_quarters = float(int(input("How many quarters?: "))*0.25)
    amount_pennies = float(int(input("How many pennies?: ")) * 0.01)
    amount_nickles = float(int(input("How many nickels?: ")) * 0.05)
    amount_dimes = float(int(input("How many dimes?: ")) * 0.10)

    Total_deposit = amount_dimes+ amount_nickles+amount_pennies + amount_quarters

    return Total_deposit

def resource_updater(chosen_coffee):
    global Total_Money
    order_ingredients = chosen_coffee['ingredients']
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    Total_Money += chosen_coffee['cost']



def make_coffee(chosen_coffee):
    if resource_checker(chosen_coffee['ingredients']):
        deposited_money = deposit_money(chosen_coffee)
        print(f"Deposited money {deposited_money}")
        if check_transaction(chosen_coffee, deposited_money):
            change = deposited_money - chosen_coffee['cost'] 
            print(f"here's your change: {change}")
            resource_updater(chosen_coffee)
            print(f"Enjoy your COFFEE..!")
        else:
            print("Transaction failed! Insufficient money...")

def coffee_machine():
    global Total_Money
    keep_running = True
    while keep_running:
        ask = input("What would you like? 'espresso', 'latte', 'cappuccino', or 'report' to get a report, or 'cancel' to cancel:\nEnter: ").lower()
        if ask == 'espresso' or ask == 'latte' or ask == 'cappuccino':
            make_coffee(MENU[ask])
        elif ask == 'report':
            display_report()
        elif ask == 'cancel':
            keep_running = False
        else:
            print("Invalid input. Please enter 'espresso', 'latte', 'cappuccino', 'report', or 'cancel'.")

coffee_machine()
        
#Improvised by me!!!!