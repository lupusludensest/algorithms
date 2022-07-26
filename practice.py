# # Disney code interview dt 10 june 2022
# nums = [2,7,11,15]
# def wrkwlst(nums):
#     nlst=[]
#     nnlst=[]
#     for i in range(len(nums)):
#         if (nums[i-1] + nums[i]) == 9:
#             nlst.append(nums[i-1]), nlst.append(nums[i]),nnlst.append(i-1), nnlst.append(i)
#     return f'Elements: \t{nlst}\nIndexes: \t{nnlst}'
# print(wrkwlst(nums))

# # Decimal to binary
# dec = int(input('Input decimal: '))
# bnr=''
# while dec > 0:
#     bnr += str(dec % 2)
#     dec = dec // 2
# bnr = bnr[::-1]
# print(bnr)

# # Count even and odd number in the integer
# def cntevod(num = int(input('Énter the integer: '))):
#     print(f'You entered integer: {num}')
#     lsnm = list(map(int, str(num)))
#     print(f'We have a list {lsnm}, {type(lsnm)}')
#     ev = []
#     od = []
#     for e in lsnm:
#         if e % 2 == 0:
#             ev.append(e)
#         else:
#             od.append(e)
#     return f'Ev: {len(ev)} = {ev}\nOd: {len(od)} = {od}'
# print(cntevod())

# # Count char in the string
# st = str(input('Enter the string: '))
# print(f'You entered the string: {st}')
# ch = str(input('Enter the char to count the char in string: '))
# print(f'You have {ch} to count in the string')
# def cntchr(st, ch):
#     cntr = 0
#     for e in st:
#         if e == ch:
#             cntr += 1
#         else:
#             cntr += 0
#     return f'We have "{ch}" repeated "{cntr}" times'
# print(cntchr(st, ch))

# # Factorial n! of integer
# def fctrl(num = int(input('Enter the integer: '))):
#     if num == 0:
#         return f'Factorial of "{num}" = "1"'
#     fctrl = 1
#     for e in range(1, num + 1):
#         fctrl *= e
#     return f'Factorial of "{num}" = "{fctrl}"'
# print(fctrl())

# answers = ['A', 'B', '', 'D']
# for answer in answers:
#     if answer == '':
#         print('Incomlete')
#         break
#     print(answer)
# print('Loop is done')

# list1 = [1, 2, 3, 4, 5]
# def fnd_n_lst(list1):
#     ev = []
#     od = []
#     for i in list1:
#         if i % 2 == 0:
#             ev.append(i)
#         else:
#             od.append(i)
#     return f'Even: {ev}, total: {len(ev)},\nOdd:{od}, total: {len(od)}'
#
# print(fnd_n_lst(list1))


# # Iterate as an elements
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def itrsel():
#     i = []
#     for e in lst1:
#         i.append(e)
#     return i, type(i)
# print(itrsel())

# # Iterate as indexes
# lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# def itrsin():
#     i = []
#     for e in range(0, len(lst2)):
#         i.append(e)
#     return i, type(i)
# print(itrsin())

# print(f'1\n')

# alpha = "abcdefghijklmnopqrstuvwxyz"
# input = "aaaabbbccdddd"
#
# for char in alpha.lower():
#     count = input.count(char)
#     if count > 0:
#         print(str(count) + char, end='')


# print(f'2\n')

# from collections import Counter

# input = 'aaaabbbccdddd'
# count = Counter(input)
# res = ''
# print(res.join(list(map(lambda b: str(count[b]) + b, count))))

# print(f'3\n')

# input = 'aaaabbbccdddd'
# def cntchrs(input):
#     a = b = c = d = 0
#     for e in input:
#         if e == 'a':
#             a += 1
#         elif e == 'b':
#             b += 1
#         elif e == 'c':
#             c += 1
#         else:
#             d += 1
#     return f'{a}{e}{b}{e}{c}{e}{d}{e}'
#
# print(cntchrs(input))

# print(f'4\n')
#
# input = 'aaaabbbccdddd'
# def cntchrs(input):
#     res = ''
#     for e in input:
#         if input.count(e) > 0:
#             res += (str(input.count(e)) + e)
#     res += (str(input.count(e)) + e)
#     return f'{res}'
#
# print(cntchrs(input))

# input = 'aaaabbbccdddd'
# # expected output is: output = '4a3b2c4d'
# def cntchrs(input):
#   char = input[0]
#   countLetter = 1
#   output = ''
#   for i in range(1, len(input)):
#     if input[i - 1] == input[i]:
#       countLetter += 1
#     elif input[i - 1] != input[i]:
#       output += (str(countLetter) + char)
#       char = input[i]
#       countLetter = 1
#
#   output += str(countLetter) + char
#   return output

# print(cntchrs(input))

# input = 'aaaabbbccdddd'
# # expected output is: output = '4a3b2c4d'
# def cntltrs(input):
#     if input == '':
#       return ''
#     output = ''
#     cur = ''
#     for l in input:
#         if cur == '':
#           cur = l
#         elif cur[0] == l:
#           cur+=l
#         else:
#           output += f"{len(cur)}{cur[0]}"
#           cur=l
#     output += f"{len(cur)}{cur[0]}"
#     return f'{output}'
# print(cntltrs(input))

# input = 'aaaabbbccddddaaaa'
# # expected output is: output = '4a3b2c4d'
# def cntchars(input):
#     letter = input[0]
#     countLetter = 1
#     res = ''
#     for i in range(1, len(input)):
#         if input[i] == input[i - 1]:
#             countLetter += 1
#         elif input[i] != input[i - 1]:
#             res += str(countLetter) + letter
#             letter = input[i]
#             countLetter = 1
#     res += str(countLetter) + letter
#     return res
# print(cntchars(input))

# input = 'aaaabbbccddddaaaa'
# output = {}
#
# for i in input:
#     output[i] = input.count(i)

# print(output)

# input = 'aaaabbbccddddaaaa'
# def cntchrs(input):
#     output = {}
#     for ind in input:
#         output[ind] = input.count(ind)
#     return output
#
# print(cntchrs(input))

# input = 'aaaabbbccdddd'
# # expected output is: output = '4a3b2c4d'
# def cntltrs(input):
#  output = ''
#  for n in range(0, len(input)):
#     if (len(output)==0 or input[n] != output[-1]):
#      if input.count(input[n]) > 0 and input[n - 1] == input[n]:
#         output += (str(input.count(input[n - 1])) + input[n - 1])
#  return f'{output}'
# print(cntltrs(input))

# print('Пиши свое число и я его прибавлю')
# first = round(float(input('Enter the number: ')), 2)
# print(f'Ответ: 1 + {first} = {1 + first}')


# a=float('1.93')
# b=float('1,93')
# print(a,b)

# print(444//110) # 4
# print(444//100) # 4
# print(444%100) # 44

# # find min and max elements in list
# lst = [1,2,3,4,5,6,7,8,9,10,-100,100]
# def mnMx(lst):
#     mn = mx = lst[0]
#     for el in lst:
#         if el < mn:
#             mn = el
#         elif el > mx:
#             mx = el
#     return f'Mn: {mn}: Mx:{mx}'
# print(mnMx(lst))

# # generate list from number n < m
# n, m = 5, 10
# def gnrtLstfrmNmbrsNm(n, m):
#     lst = []
#     for el in range(n, m + 1):
#         lst.append(el)
#     return lst
# print(gnrtLstfrmNmbrsNm(n, m))

# # find word with the length more than 5 from list of words
# lst = ["Sandra", "Dorothy", "Paul", "Aristarkh", "Betty", "John", "Jenny", "Alexander", 1234, True]
# def fndWrdsMrFv(lst):
#     nStr = []
#     mrFv = []
#     lsFv = []
#     for ind in range(0, len(lst)):
#         if type(lst[ind]) != str:
#             nStr.append(lst[ind])
#         elif len(lst[ind]) > 5:
#             mrFv.append(lst[ind])
#         elif len(lst[ind]) <= 5:
#             lsFv.append(lst[ind])
#
#     return f'Nstr: {nStr}\nMrfv: {mrFv}\n'f'Lsfv: {lsFv}'
#
# print(fndWrdsMrFv(lst))

# # find index of first negative element in the list of numbers
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,-11, 1234, -123]
# def fndFrstNgElmnt(lst):
#     frstNgtvElmnt = ''
#     for i in range(0, len(lst)):
#         if lst[i] < 0:
#             frstNgtvElmnt += str(i)
#             break
#     return f'frstNgtvElmnt: {frstNgtvElmnt}'
#
# print(fndFrstNgElmnt(lst))

# # reverse the elements of the list
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,-11, 1234, -123]
# def rvrsElmntsLst(lst):
#     for e in lst:
#         if type(e) == int:
#             rlst = lst[::-1]
#         return rlst
#
# print(rvrsElmntsLst(lst))

# def replace_word(string, s, n_word):
#     r = []
#     l = string.split()
#     for word in l:
#         if word.lower() == s:
#             r.append(n_word)
#         else:
#             r.append(word)
#     return ' '.join(r)
#
#
# print(replace_word('Hello heLlo PYthon pasv', 'hello', 'HI'))

# def expression_matter(a, b, c):
#     lst = []
#     lst.append(a)
#     lst.append(b)
#     lst.append(c)
#     max = lst[0]
#     for e in lst:
#         if e > max:
#             max = e
#     return max
# print(expression_matter(3, 4, 5))

# def expression_matter(a, b, c):
#     lst = []
#     aa = (a + b) * c
#     bb = a + b + c
#     cc = a * b * c
#     dd = a * (b + c)
#     lst.append(aa)
#     lst.append(bb)
#     lst.append(cc)
#     lst.append(dd)
#     max = lst[0]
#     for e in lst:
#         if e > max:
#             max = e
#     return max
# print(expression_matter(3, 4, 5))

# def discover_original_price(discounted_price, sale_percentage):
#     return round(float(discounted_price / (100 - sale_percentage) * 100), 2)
# print(discover_original_price(373.85,11.2)) # 421

# def two_decimal_places(number):
#     return int(number * 100) / 100.0
# print(two_decimal_places(10.1289767789))

# import math
# def square_area(A):
#     return round((A*4/(2*math.pi))**2, 2)
# print(square_area(14.05)) # 80

# S = L**2 : (4 × π), где L — это длина окружности

# import math
# def square_area(A):
#     return round((A * 2 / math.pi) ** 2, 2)
# print(square_area(14.05)) # 80

# def enough(cap, on, wait):
#     if wait + on == cap:
#         return cap - wait - on
#     elif wait + on > cap:
#         return (cap - on - wait) * -1
#     else:
#         return 0
# print(enough(100, 60, 50)) # 10
# print(enough(10, 5, 5)) # 0

# def get_planet_name(id):
#     if id == 1:
#         return "Mercury"
#     if id == 2:
#         return "Venus"
#     if id == 3:
#         return "Earth"
#     if id == 4:
#         return "Mars"
#     if id == 5:
#         return "Jupiter"
#     if id == 6:
#         return "Saturn"
#     if id == 7:
#         return "Uranus"
#     if id == 8:
#         return "Neptune"
#     else:
#         return "Not valid ID"
# print(get_planet_name(9))

# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)
# print(get_planet_name(3))

# def triangular(n):
#     if n >= 1 and type(n) == int:
#         return n * (n + 1) // 2
#     else:
#         return 0
# print(triangular(0))
# print(triangular(1))
# print(triangular(2))
# print(triangular(3))
# print(triangular(4))
# print(triangular(5))
# print(triangular(-9))
# print(triangular(69179757194))

# def triangular(n):
#     if n < 1 and type(n) == int:
#         return 0
#     else:
#         return n * (n + 1) // 2
# print(triangular(0))
# print(triangular(1))
# print(triangular(2))
# print(triangular(3))
# print(triangular(4))
# print(triangular(5))
# print(triangular(-9))
# print(triangular(69179757194))

# def triangular(n: int) -> int:
#     return n * (n + 1) // 2 if n > 0 else 0 # floor division is an answer
# print(triangular(0))
# print(triangular(1))
# print(triangular(2))
# print(triangular(3))
# print(triangular(4))
# print(triangular(5))
# print(triangular(-9))
# print(triangular(69179757194))

# lst = [1, 2, 'dod', {"id": 4, "name": 'George'}]
# def shr_lst(lst):
#     nmrs = []
#     strn =[]
#     els = []
#     for e in lst:
#         if type(e) == int:
#             nmrs.append(e)
#         elif type(e) == str:
#             strn.append(e)
#         elif type(e) == dict:
#             els.append(e)
#         else:
#             return f'Wrong input'
#     return f'Numbers: {nmrs}\nStrings: {strn}\nElse: {els}'
# print(shr_lst(lst))

# l1 = [-5, 10, 3, 4, 0, 2,-5]

# str1 = 'abcabcbb'
# str2 = 'pwwkew'
# def lng_str(str1, str2):
#     if len(str1) > len(str2):
#         return f'{str1}'
#     else:
#         return f'{str2}'
#
# print(lng_str(str1, str2))

# def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
#     if dolphin == True and pontoon_distance / you_speed < shark_distance / shark_speed * 0.5:
#         print(pontoon_distance / you_speed, shark_distance / shark_speed * 0.5)
#         return f'Alive!'
#     elif dolphin == True and pontoon_distance / you_speed < shark_distance / shark_speed:
#         print(pontoon_distance / you_speed, shark_distance / shark_speed)
#         return f'Alive!'
#     elif dolphin == True and pontoon_distance / you_speed >= shark_distance / shark_speed * 0.5:
#         print(pontoon_distance / you_speed, shark_distance / shark_speed * 0.5)
#         return f'Shark Bait!'
#     elif dolphin == True and pontoon_distance / you_speed >= shark_distance / shark_speed:
#         print(pontoon_distance / you_speed, shark_distance / shark_speed)
#         return f'Shark Bait!'
#
#     elif dolphin == False and pontoon_distance / you_speed < shark_distance / shark_speed:
#         print(pontoon_distance / you_speed, shark_distance / shark_speed)
#         return f'Alive!'
#     elif dolphin == False and pontoon_distance / you_speed >= shark_distance / shark_speed:
#         print(pontoon_distance / you_speed, shark_distance / shark_speed * 0.5)
#         return f'Shark Bait!'
#     else:
#
#         return f'Shark Bait!'
# print(shark(12, 50, 4, 8, True))
# print(shark(7, 55, 4, 16, True))
# print(shark(24, 0, 4, 8, True))

# def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
#     if dolphin == True:
#         shark_time = shark_distance / (shark_speed * 0.5)
#     else:
#         shark_time = shark_distance / shark_speed
#     if pontoon_distance / you_speed < shark_time:
#         return f'Alive!'
#     else:
#         return f'Shark Bait!'
# print(shark(12, 50, 4, 8, True))
# print(shark(7, 55, 4, 16, True))
# print(shark(24, 0, 4, 8, True))

# def shark(d1, d2, v1, v2, x):
#     return "Alive!" if d1 / v1 < d2 / v2 * (x + 1) else "Shark Bait!"
# print(shark(12, 50, 4, 8, True))
# print(shark(7, 55, 4, 16, True))
# print(shark(24, 0, 4, 8, True))

# gather all repeatable elements together and count them
# lst = ['Dana', 'Pete', 'John', 'Raju', 'Elsa', 'Raju', 'Raju', 'Raju', 'Raju', 'Raju']
# def cnt_wrds(lst):
#     counter = {}
#     for el in lst:
#         counter[el] = counter.get(el, 0) + 1
#     doubles = {element: count for element, count in counter.items() if count > 1}
#     return doubles
# print(cnt_wrds(lst))

# # gather all repeatable elements together and count them
# lst = ['Dana', 'Pete', 'John', 'Raju', 'Elsa', 'Raju', 'Raju', 'Raju', 'Raju', 'Raju']
# def cnt_wrds(lst):
#     cntr = 0
#     dbls = []
#     for i in range(len(lst)):
#         if lst.count(lst[i]) > 1:
#             cntr += 1
#             dbls.append(lst[i])
#     return cntr, dbls
# print(cnt_wrds(lst))

# ## expected
# # I love you
# # a little
# # a lot
# # passionately
# # madly
# # not at all
# # When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# def how_much_i_love_you(nb_petals):
#     means = ["not at all", "I love you", "a little", "a lot", "passionately", "madly"]
#     return means[nb_petals % 6]
# print(how_much_i_love_you(7)) # I love you 7 % 6 == 1
# print(how_much_i_love_you(6)) # not at all 6 % 6 == 0
# print(how_much_i_love_you(5)) # madly 5 % 6 == 0.8333333333333333
# print(how_much_i_love_you(4)) # passionately 4 % 6 == 0.6666666666666667
# print(how_much_i_love_you(3)) # a lot 3 % 6 == 0.5
# print(how_much_i_love_you(2)) # a little 2 % 6 == 0.3333333333333333
# print(how_much_i_love_you(1)) # I love you 1 % 6 == 0.1666666666666667

# ## expected
# # I love you
# # a little
# # a lot
# # passionately
# # madly
# # not at all
# # When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# def how_much_i_love_you(nb_petals):
#     lst = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
#     rmndr = nb_petals % len(lst)
#     return lst[rmndr - 1]
# print(how_much_i_love_you(7)) # I love you 7 % 6 == 1
# print(how_much_i_love_you(6)) # not at all 6 % 6 == 0
# print(how_much_i_love_you(5)) # madly 5 % 6 == 0.8333333333333333
# print(how_much_i_love_you(4)) # passionately 4 % 6 == 0.6666666666666667
# print(how_much_i_love_you(3)) # a lot 3 % 6 == 0.5
# print(how_much_i_love_you(2)) # a little 2 % 6 == 0.3333333333333333
# print(how_much_i_love_you(1)) # I love you 1 % 6 == 0.1666666666666667

# def apple(x):
#     if int(x) ** 2 > 1000:
#         return f'It\'s hotter than the sun!!'
#     else:
#         return f'Help yourself to a honeycomb Yorkie for the glovebox.'
# print(apple(50))

# def apple(x):
#   return "It's hotter than the sun!!" if int(x) ** 2 > 1000 else  "Help yourself to a honeycomb Yorkie for the glovebox."
# print(apple(50))

# b = bool(input('Enter your data: '))
# a = 3
# # print(4) if (a < b) else print(100)
# print(f'b = {b}, a = {a}')
# if a > b :
#   print(4)
# else:
#   print(100)

# def apple(x):
#   if (x ** 2) > 1000:
#     return f'It\'s hotter than the sun!!'
#   else:
#     return f'Help yourself to a honeycomb Yorkie for the glovebox.'
# print(apple(1001))


# def apple(x):
#   if (x ** 2) > 1000:
#     return f"It's hotter than the sun!!"
#   else:
#     return f"Help yourself to a honeycomb Yorkie for the glovebox."
# print(apple(1001))

# def sum_str(a, b):
#   if b == "":
#     b = 0
#   if a == "":
#     a = 0
#   return str(int(a) + int(b))
# print(sum_str("9", ""))
# print(sum_str("", "9"))
# print(sum_str("9", "9"))
# print(sum_str("", ""))

# def sum_str(a, b):
#   try:
#     return str(int(a) + int(b))
#   except ValueError:
#     return '0' if a + b == '' else a + b
# print(sum_str("9", ""))
# print(sum_str("", "9"))
# print(sum_str("9", "9"))
# print(sum_str("", ""))

# def get_grade(s1, s2, s3):
#   if 90 <= (s1 + s2 + s3) / 3 <= 100:
#     return 'A'
#   elif 80 <= (s1 + s2 + s3) / 3  < 90:
#     return 'B'
#   elif 70 <= (s1 + s2 + s3) / 3  < 80:
#     return 'C'
#   elif 60 <= (s1 + s2 + s3) / 3  < 70:
#     return 'D'
#   elif 0 <= (s1 + s2 + s3) / 3  < 60:
#     return 'F'
# print(get_grade(95, 90, 93))

# def get_grade(s1, s2, s3):
#   mean = (sum([s1, s2, s3])) / 3
#   if 90 <= mean <= 100: return 'A'
#   if 80 <= mean < 90: return 'B'
#   if 70 <= mean < 80: return 'C'
#   if 60 <= mean < 70: return 'D'
#   if 0 <= mean < 60: return 'F'
# print(get_grade(95, 90, 93))

# def summation(num):
#   return sum(list(range(1, num + 1)))
# print(summation(8))

# summation = lambda num: sum(list(range(1, num + 1)))
# print(summation(8))

# summation = lambda n: (n*n+n)/2
# print(summation(8))

# def summation(num):
#   r = 0
#   for e in range(0, num + 1):
#     r = r + e
#   return r
# print(summation(8))

# lst1 = [1, 2, 3, 4]
# lst2 = [5, 6, 7, 8]
# lst12tpl = tuple(lst1 + lst2)
# print(lst12tpl, type(lst12tpl))

# def hllwrld():
#   return f'Hello world!'
# print(hllwrld())

# def switch_it_up(number):
#     if number == 1:
#         return"One"
#     elif number == 2:
#         return "Two"
#     elif number == 3:
#         return "Three"
#     elif number == 4:
#         return "Four"
#     elif number == 5:
#         return "Five"
#     elif number == 6:
#         return "Six"
#     elif number == 7:
#         return "Seven"
#     elif number == 8:
#         return "Eight"
#     elif number == 9:
#         return "Nine"
#     elif number == 0:
#         return "Zero"
#     else:
#         return "Wrong input"
# print(switch_it_up(5))

# def switch_it_up(n):
#     return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
# print(switch_it_up(5))

# import math
# def movie(card, ticket, perc):
#     # ticket_num
#     ticket_num = 0
#     sys_a = 0
#     sys_b = card
#     sys_b_prev = ticket
#     # while loop sys A > loop sys B:
#     while math.ceil(sys_b) >= sys_a:
#         # sys A math
#         sys_a += ticket
#         # sys B math
#         sys_b_prev *= perc
#         sys_b += sys_b_prev
#         ticket_num += 1
#     # iterate ticket_num
#     return ticket_num
# print(movie(500, 15, 0.9))
# print(movie(100, 10, 0.95))

# import math
# def movie(card, ticket, perc):
#     # ticket_num
#     ticket_num = 0
#     sys_a = 0
#     sys_b_prev = ticket
#     # while loop sys A > loop sys B:
#     while math.ceil(card) >= sys_a:
#         # sys A math
#         sys_a += ticket
#         # sys B math
#         sys_b_prev *= perc
#         card += sys_b_prev
#         ticket_num += 1
#     # iterate ticket_num
#     return ticket_num
# print(movie(500, 15, 0.9))
# print(movie(100, 10, 0.95))

# def rain_amount(mm):
#     if mm < 40:
#          return f"You need to give your plant {40 - mm}mm of water"
#     else:
#          return f"Your plant has had more than enough water for today!"
# print(rain_amount(100))
# print(rain_amount(39))

# def calculator(x, y, op):
#     # x and y - operands, op - operator
#     if (type(y) == type(x) != str) and (str(op) in "+-*/"):
#       if op == '+':
#           return x + y
#       elif op == '-':
#           return x - y
#       elif op == '*':
#           return x * y
#       elif op == '/':
#           return x / y
#     else:
#       return 'unknown value'
# print(calculator(6, 2, '+'))
# print(calculator(4, 3, '-'))
# print(calculator(5, 5, '*'))
# print(calculator(5, 4, '/'))
# print(calculator(6, 2, '&'))
# print(calculator(6, "$", '+'))

# def calculator(x, y, op):
#   return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'
# print(calculator(6, 2, '+'))
# print(calculator(4, 3, '-'))
# print(calculator(5, 5, '*'))
# print(calculator(5, 4, '/'))
# print(calculator(6, 2, '&'))
# print(calculator(6, "$", '+'))

# def find_slope(points): # m = (y2 - y1) / (x2 - x1) a:x1    b:y1    c:x2    d:y2 points = [a,b,c,d]
#   if points[2] - points[0] != 0:
#     return str(round((points[3] - points[1]) / (points[2] - points[0])))
#   else:
#     return "undefined"
# print(find_slope([-10,6,-10,3]))
# print(find_slope([19,3,20,3]))
# print(find_slope([-7,2,-7,4]))
# print(find_slope([10,50,30,150]))

# def draw_stairs(n):
#   res = ''
#   for e in range(0, n - 1):
#     res += ' ' * e + 'I\n'
#   res += ' ' * (n - 1) + 'I'
#   return res
# print(draw_stairs(3))

# numpy array
import numpy as np
import pandas as pd
# a = np.array([1, 4, 5, 8], float)
# print(a)
# print(type(a))
#
# print(a[:2])
# print(a[3])
# print(a[0])
# print(a)

# b = np.array([[1, 2, 3], [4, 5, 6]], float)
# print(b)
# print(b[0,0])
# print(b[0,1])
# print(b[1,:])
# print(b[:,2])
# print(b[-1:, -2:])
# print(b.shape) # shape возвращает количество строк и столбцов в матрице
# print(b.dtype) # dtype возвращает тип переменных, хранящихся в массиве  float64, это числовой тип данных в numpy, который используется для хранения вещественных чисел двойной точности
# print(len(b)) # len возвращает длину первого измерения (оси)
# print(2 in b) #  in используется для проверки на наличие элемента в массиве
# print(0 in b)

# c = np.array(range(10), float)
# print(c)
# c = c.reshape((5, 2)) # 5 листов по 2 элемента метод reshape создает новый массив, а не модифицирует оригинальный
# print(c)
# print(c.shape)

# d = np.array([1, 2, 3], float) # copy используется для создания копии существующего массива в памяти
# e = d
# print(e)
# f = d.copy()
# print(f)
# d[0] = 0
# print(d)
# print(e)
# print(f)

# cписки можно тоже создавать с массивов
# a = np.array([1, 2, 3], float)
# s = a.tobytes()
# print(s)
# s = np.frombuffer(s)
# print(s)

# lst1 = list(map((lambda x:x**3), range(5)))
# lst2 = [x**3 for x in range(5)]
# print(f'{lst1}\n{lst2}')

# import math
# print(math.fabs(-45.24)) # fabs() method returns the absolute value of a number, as a float. Absolute denotes a non-negative number. This removes the negative sign of the value if it has any. Unlike Python abs(), this method always converts the value to a float value.

# def draw_stairs(n):
#     r = ''
#     for e in range(0, n - 1):
#         r += ' ' * e + 'I\n'
#     r += ' ' * (n - 1) + 'I'
#     return r
# print(draw_stairs(3**3))

# str1 = "Geeks For Geeks"
# def cntwrfs(str1):
#     res = 0
#     res1 = 0
#     for e in str1.split():
#         if e == 'For':
#             res += 1
#         elif e == 'Geeks':
#             res1 += 1
#     return res, res1
# print(cntwrfs(str1))

# str1 = "Geeks For Geeks"
# def cntwrfs(str1):
#     res = 0
#     res1 = 0
#     lsstr1 = list(str1.split())
#     for i in range(0, len(lsstr1)):
#         if lsstr1[i - 1] == lsstr1[i]:
#             res += 1
#         elif lsstr1[i - 1] != lsstr1[i]:
#             res1 += 1
#     return res, res1
# print(cntwrfs(str1))

# n = 100
# def nmbrs_n(n):
#     res = []
#     for e in range(1, n + 1):
#         res.append(e)
#     return res
# print(nmbrs_n(n))

# n_mmbr = str(input('Enter the name: '))
# def add_nm(n_mmbr):
#     ls_nms = ['Kate', 'Vic']
#     if n_mmbr not in ls_nms:
#         ls_nms.append(n_mmbr)
#         return ls_nms
#     else:
#         return f'{n_mmbr} is already here.'
# print(add_nm(n_mmbr))

# a_list =['Don\'t', 'do', 'this', 'the', '"C"', 'way']
# def dnt_d_c_wy(a_list):
#     for x in a_list:
#         print(x, end = ' ')
# print(dnt_d_c_wy(a_list))

# x = ['Python', 'is', 'cool']
# def prnt_ptn_cl(x):
#     return ' '.join(x)
# print(prnt_ptn_cl(x))

# def print_nums(n):
#     i = 0
#     while i < n:
#         i += 1
#         print(i, end = '\t')
# print(print_nums(8))

def next_prime(n):
    k = n + 1
    while k:
        for i in range(2, k + 1):
            if k % i == 0:
                break
        if i == k:
            return k
            break
        else:
            k += 1
print(next_prime(0))
print(next_prime(2))
print(next_prime(3))
print(next_prime(13))
print(next_prime(181))
print(next_prime(911))









