# financial_code_name_date_of_birth
# https://progsva.ru/numfinkod.phtml

def financial_code_name_date_of_birth(your_name, day, month, year):
    letters_indexes = {'А':1, 'Б':2, 'В':6, 'Г':3, 'Д':4, 'Е':5, 'Ж':2, 'З':7,
                            'И':1, 'Й':1, 'К':2, 'Л':2, 'М':4, 'Н':5, 'О':7, 'П':8,
                            'Р':2, 'С':3, 'Т':4, 'У':6, 'Ф':8, 'Х':5, 'Ц':3, 'Ч':7,
                            'Ш':2, 'Щ':9, 'Ы':1, 'Ь':1, 'Э':6, 'Ю':7, 'Я':2,}
    your_name_list = list(your_name)
    your_name_list_str = ''
    for letter in your_name_list:
        your_name_list_str += str(letters_indexes[letter])
    your_name_list_str_int = int(your_name_list_str)
    sum_your_name_list_str_int = 0
    for i in str(your_name_list_str_int):
        sum_your_name_list_str_int += int(i)
    sum_name = 0
    for i in str(sum_your_name_list_str_int):
        sum_name += int(i)

    sum_d = 0
    for d_d in str(day):
        sum_d += int(d_d)
    sum_m = 0
    for d_m in str(month):
        sum_m += int(d_m)
    sum_y = 0
    for d_y in str(year):
        sum_y += int(d_y)
    d_d_y_y = 0
    for d_y_y in str(sum_y):
        d_d_y_y += int(d_y_y)
    day_of_birth_index = 0
    for d in str(sum_d + sum_m + sum_y):
        day_of_birth_index += int(d)


    return (f'Number of name: {sum_name}\n'
            f'Number of wealth: {day + sum_name}\n'
            f'Private code of success: {day_of_birth_index}\n'
            f'Financial code of success: {sum_d}{sum_m}{d_d_y_y}{day_of_birth_index}')

print(financial_code_name_date_of_birth('ВЯЧЕСЛАВ', 3, 7, 1970))
