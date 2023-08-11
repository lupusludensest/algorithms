# signatures or type checkers

import math

product_count = int(input('Enter the product quantity: '))
box_capacity = int(input('Enter the boxes capacity: '))
price_per_unit = float(input('Enter the price per unit: '))

def check_cuantity_capacity_price(product_count: int, box_capacity: int, price_per_unit: float):
    # Check if the input data are correct
    if type(product_count) != int or product_count < 1:
        raise AssertionError('Wrong quantity')  # Value unacceptable
    elif type(box_capacity) != int or box_capacity < 1:
        raise AssertionError('Wrong capacity')  # Value unacceptable
    elif  type(price_per_unit) != float or price_per_unit < 0.01:
        raise AssertionError('Wrong price')  # Value unacceptable

    return f'You need: {math.ceil(product_count/box_capacity)} box. \nPrice is valid.\n' # returns the result

print(check_cuantity_capacity_price(product_count, box_capacity, price_per_unit))