# Import Resources
from data import resources
from data import MENU


EARNINGS = 0.00
is_on = True
# Function to check if resources are sufficient for the order


def resource_check(order_ingredients):
    """Determines if enough resources for the order and returns true or prints inadequate resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


# Function to ask user to insert coins and then return total


def process_coins():
    """Returns the total calculated from coins inserted by customer."""
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


# Function to check transaction


def transaction_successful(client_order, total_coins):
    """Return true when the payment is accepted, or False if money is insufficient"""
    for key, value in MENU.items():
        if key == client_order:
            cost = MENU[key]["cost"]
    if cost == total_coins:
        return True
    elif cost > total_coins:
        # If not enough money, refund coins
        print(f"Sorry, that's not enough money for this item. Return ${round(total_coins,2)}")
    else:
        # TODO calculate change
        change = round((total_coins - cost), 2)
        print(f"Here is your change: ${change}")
        return True


# Function to deplete resources after successful order


def deplete_resources(order_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {order_name} ☕ Enjoy!")


# TODO The prompt should show every time action has completed, e.g. once the drink is dispensed
while is_on:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino)
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'report':
        # Print Report
        # Format resources report in printable format
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g")
        # Print money total for report
        print(f"Money: {EARNINGS}")
    elif order == 'off':
        # Turn off the Coffee Machine by entering “off” to the prompt.
        print("Machine is off for maintenance")
        is_on = False
    # Check if resources are sufficient for the order
    else:
        drink = MENU[order]
        if resource_check(order_ingredients=drink["ingredients"]):
            print("Please insert coins.")
            payment = process_coins()
            # Check that user input enough money
            if transaction_successful(order, payment):
                # Add money to earnings
                EARNINGS += MENU[order]["cost"]
                # Deplete resources
                deplete_resources(order, drink["ingredients"])
