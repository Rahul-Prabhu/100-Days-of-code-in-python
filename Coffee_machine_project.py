# TODO 1: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


# TODO 2: 2.2. Turn off the Coffee Machine by entering “off” to the prompt.


# TODO 3: 3. Print report.


# TODO 4: 4. Check resources sufficient?


# TODO 5: 5. Process coins.


# TODO 6: 6. Check transaction successful?


# TODO 7:  Make Coffee
# money_earned=0
import data
import random


def estimate_money(quarters, dimes, nickles, pennies):
    return (0.25*quarters + 0.05*nickles + 0.1*dimes + 0.01*pennies)



def update_report(coffee_flavour,money_given,change_money=0):
    global money_earned
    money_earned=money_earned+money_given-change_money
    data.resources['water']=data.resources['water']-data.MENU[coffee_flavour]['ingredients']['water']
    data.resources['coffee']=data.resources['coffee']-data.MENU[coffee_flavour]['ingredients']['coffee']
    data.resources['milk']=data.resources['milk']-data.MENU[coffee_flavour]['ingredients']['milk']


def isSufficient(money_given,coffee_flavour):
    if money_given>=data.MENU[coffee_flavour]['cost']:
        return True
    else:
        return False

def resource_sufficiency(coffee_flavour):
    if data.resources['water']<data.MENU[coffee_flavour]['ingredients']['water']:
        return 'water'
    if data.resources['coffee']<data.MENU[coffee_flavour]['ingredients']['coffee']:
        return 'coffee'
    if data.resources['milk']<data.MENU[coffee_flavour]['ingredients']['milk']:
        return 'milk'




def excess_money(money_given,coffee_flavour):
    if data.MENU[coffee_flavour]['cost']>money_given:
        return (data.MENU[coffee_flavour]['cost']-money_given)

    elif data.MENU[coffee_flavour]['cost']<money_given:
            return (money_given-data.MENU[coffee_flavour]['cost'])

    else:
        return 0


while ((data.resources['water']>0) and (data.resources['milk']>0) and (data.resources['coffee']>0)):

    coffee_flavour = input('What would you like? (espresso/latte/cappuccino):')

    if coffee_flavour == 'report':
        print(f"water:{data.resources['water']}ml\n "
              f"milk:{data.resources['milk']}ml\n"
              f"coffee:{data.resources['coffee']}g\n"
              f"Money:${money_earned}\n")
    if coffee_flavour not in ['espresso','latte','cappuccino']:
        continue

    if resource_sufficiency(coffee_flavour):
        print(f'Sorry, there is not enough {resource_sufficiency(coffee_flavour)} for {coffee_flavour},Money refunded')
        continue
    print('Please insert coins.')

    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))

    money_given = estimate_money(quarters, dimes, nickles, pennies)


    if isSufficient(money_given,coffee_flavour):
        if excess_money(money_given,coffee_flavour):
            print(f"Here is ${round(excess_money(money_given,coffee_flavour),2)} in change.")
            print(f"Here is your {coffee_flavour} ☕️. Enjoy!")
            change_money=excess_money(money_given,coffee_flavour)
        else:
            print(f"Here is your {coffee_flavour} ☕️. Enjoy!")

    else:
        print(f"Sorry that's not enough money. Money refunded.")

    if change_money:
        update_report(coffee_flavour, money_given,change_money)


print(f"water:{data.resources['water']}ml\n "
              f"milk:{data.resources['milk']}ml\n"
              f"coffee:{data.resources['coffee']}g\n"
              f"Money:${money_earned}\n")