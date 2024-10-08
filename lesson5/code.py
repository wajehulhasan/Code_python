# if else examples
# Comparison Operators
# a < 2 less than
# a > 2 greater than
# a == 2 equal to
# a != 2 not equal to
# a <= 2 less than or equal to
# a >= 2 greater than or equal to


item_price = int(input('Please enter the item price: '))
quantity = input('Please enter the quantity: ')
total_cost = (item_price) * int(quantity)  # Multiply price by quantity
print('''\nThe Gold card has 10% Discount
The silver has 5% Discount
Cash has no discount
''')
user_choice = input('Please enter your mode of payment, cash or card? ')

if user_choice == 'card':
    card_type = input('Gold or Silver? ')
    if card_type == 'Gold':
        total_cost1 = total_cost * 0.90  # Apply 10% discount
        print('Your total cost was', total_cost,'After discount it is', total_cost1)
    elif card_type == 'Silver':
        total_cost1 = total_cost * 0.95  # Apply 5% discount
        print('Your total cost is', total_cost)
elif user_choice == 'cash':
    print('you are eligible for no discount')
    print('Your total cost is', total_cost)
else:
    print('Invalid mode of payment, please choose cash or card')




# Match case

age = int(input('Please enter your age'))

match age:

    case 0:
        print('you are not even born maybe')
    case 10:
        print('you are a teenager')
    case 90:
        print('you are close to death')
    case _:
        print('your age is', age)
