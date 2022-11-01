def get_result_arithmetic_operations(first_number: int, second_number: int) -> tuple:
    sum_ = first_number + second_number
    multiplication = first_number * second_number
    difference = first_number - second_number
    division = round(first_number / second_number, 2)
    return (f'Sum: {sum_}, Mult: {multiplication}, Diff: {difference}., Divis: {division}')

print(get_result_arithmetic_operations(5.5, 3))