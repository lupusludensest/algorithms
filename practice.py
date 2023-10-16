# # 20 sep 2023, wed. Practice for Disney Python interview
#
# str_a = 'Hello, dude'
# print(str_a, type(str_a))
#
# int_a = 123
# print(int_a, type(int_a))
#
# flt_a = 123.123
# print(flt_a, type(flt_a))
#
# false_a = str_a == int_a
# print(false_a, type(false_a))
#
# true_a = str_a == 'Hello, dude'
# print(true_a, type(true_a))
#
# lst_a = [1, 'one', 123.123, str_a == int_a]
# print(lst_a, type(lst_a))
#
# tuple_a = tuple(lst_a)
# print(tuple_a, type(tuple_a))
#
# dict_a = {"id": 1, "name": "vic", "age": 24}
# print(dict_a, type(dict_a))
#
# set_a = set(dict_a)
# print(set_a, type(set_a))
#
# concatenation_a = str_a + ' ' + "Concatenation"
# print(concatenation_a)
#
# for i in range(-2, 2):
#     print(i, end = '; ')
#
# print('\n')
#
# for n in range(8, -8, -1):
#     print(n, end = '; ')
#
# print('\n')
#
# i = 0
# while i < 10:
#     i += 1
#     print(i, end = '; ')
#
# print('\n')
#
# def foo(n, m):
#     return n ** m
#
# print(foo(2, 2))
#
# class employee:
#     def __init__(self, firstname, lastname, salary):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.salary = salary
#         self.email = self.firstname + "." + self.lastname + "@gmail.com"
#
#     def giveRaise(self, salary):
#         self.salary = salary
#
# class developer(employee):
#     def __init__(self, firstname, lastname, salary, programming_language):
#         super().__init__(firstname, lastname, salary)
#         self.prog_langs = programming_language
#
#     def addLanguage(self, lang):
#         self.prog_langs += [lang]
#
# emploee1 = employee("John", "Smith", 80000)
#
# print(emploee1.salary, emploee1.email)
#
# emploee1.giveRaise(100000)
#
# print(emploee1.salary, emploee1.email)
#
# dev1 = developer("Joe", "Montana", 110000, ["Python", "C"])
#
# print(dev1.salary, dev1.email)
#
# dev1.giveRaise(125000)
#
# print(dev1.salary, dev1.email)
#
# dev1.addLanguage("Java")
#
# print(dev1.prog_langs)

# import BaseTest
#
#
# # !!! Do not create your own WebDriver. !!!
# #
# # You can copy credentials from here:
# #  - login@codility.com    password
# #  - unknown@codility.com  password
#
#
# # code challenge https://app.codility.com/c/feedback/87GWG3-PZ6/ Abhishek Srivastav Sr. Technical Recruiter asrivastav@arrowcore.com M:- 678-400-0101
# class LoginPageTest(BaseTest.BaseTest):
#     # 1
#     def testLoginFormPresent(self):
#         # below you can find already setup webDriver as self.driver
#         # email fld and password fld are here on the page
#         email_fld = self.driver.find_element_by_id("email-input")
#         assert len(str(email_fld.text)) == 0
#
#         pswd_fld = self.driver.find_element_by_id("password-input")
#         assert len(str(pswd_fld.text)) == 0
#
#     # 2
#     def test_empthFldVld(self):
#         email_fld = self.driver.find_element_by_id("email-input")
#         # assert email_fld == len(email_fld.text) # is not None #
#         value_email_fld = email_fld.get_attribute('value')
#         assert value_email_fld == ''
#
#         pswd_fld = self.driver.find_element_by_id("password-input")
#         # assert pswd_fld == len(pswd_fld.text) # is not None
#         value_pswd_fld = email_fld.get_attribute('value')
#         assert value_pswd_fld == ''
#
#     # 3
#     def test_wrngCrdntls(self):
#         email_fld = self.driver.find_element_by_id("email-input")
#         email_fld.clear()
#         email_fld.send_keys("unknown@codility.com")
#
#         pswd_fld = self.driver.find_element_by_id("password-input")
#         pswd_fld.clear
#         pswd_fld.send_keys('unknown@codility.com')
#
#         lgn_btn = self.driver.find_element_by_id("login-button")
#         lgn_btn.click()
#
#         err_msg = self.driver.find_element_by_id("messages")
#         assert "You shall not pass! Arr!" == err_msg.text
#
#     # 4
#     def test_emlsVldtd(self):
#         email_fld = self.driver.find_element_by_id("email-input")
#         email_fld.clear()
#         email_fld.send_keys("unknowncodility.com")
#         pswd_fld = self.driver.find_element_by_id("password-input")
#         pswd_fld.clear
#         pswd_fld.send_keys('qwerty')
#         lgn_btn = self.driver.find_element_by_id("login-button")
#         lgn_btn.click()
#
#         err_msg = self.driver.find_element_by_id("messages")
#         assert "Enter a valid email" == err_msg.text
#
#     # 5
#     def test_rghtCrdntls(self):
#         # from selenium.webdriver.support.ui import WebDriverWait
#         # from selenium.webdriver.support import expected_conditions as EC
#         # from selenium.webdriver.common.by import By
#         # from selenium import webdriver
#
#         email_fld = self.driver.find_element_by_id("email-input")
#         email_fld.clear()
#         email_fld.send_keys("login@ncodility.com")
#
#         pswd_fld = self.driver.find_element_by_id("password-input")
#         pswd_fld.clear
#         pswd_fld.send_keys('password')
#         lgn_btn = self.driver.find_element_by_id("login-button")
#         lgn_btn.click()
#
#         # WLCM_MSG = (By.XPATH, "//div[@class='message success']")
#         wlcm_msg = self.driver.find_element_by_id("container") # wait.until(EC.visibility_of_element_located(WLCM_MSG))
#         assert "Welcome to Codility" == wlcm_msg.text

# # Find indexes of elements in the given array which gives summ "target" together
# lst_1 = [2, 7, 11, 15] # target  = 9
# lst_2 = [3, 2, 4] # target  = 6
# lst_3 = [3, 3 ] # target  = 6
#
# def two_sum(lst, target):
#     # 1 brute force
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             # compare values from both loops and their indexes are not the same
#             if lst[i] + lst[j] == target and i != j:
#                 return f'{i},{j}'
#
# print(two_sum(lst_1, 9))
# print(two_sum(lst_2, 6))
# print(two_sum(lst_3, 6))
#
# print('*' * 30)
# def two_sum(lst, target):
#     # 2 faster way or more efficient
#     hash = {}
#     for i, num in enumerate(lst):
#         diff = target - num
#         if diff in hash:
#             return f'{hash[diff]},{i}'
#         hash[num] = i
#     return None
#
#
# print(two_sum(lst_1, 9))
# print(two_sum(lst_2, 6))
# print(two_sum(lst_3, 6))

# Code challenge 16 October 2023
# Имеется строка '1h 45m,360s,25m,30m 120s,2h 60s'. Необходимо посчитать общее кол-во
# минут, содержащееся в строке.
import re

# time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# def calculate_total_minutes(time_string):
#   times = time_string.split(',')
#
#   total_minutes = 0
#
#   for time in times:
#
#     hours = 0
#     minutes = 0
#     seconds = 0
#
#     match = re.search('(\d+)h', time)
#     if match:
#       hours = int(match.group(1))
#
#     match = re.search('(\d+)m', time)
#     if match:
#       minutes += int(match.group(1))
#
#     match = re.search('(\d+)s', time)
#     if match:
#       seconds += int(match.group(1))
#
#     minutes += seconds // 60
#     total_minutes += hours * 60 + minutes
#
#   return total_minutes
#
#
# print(calculate_total_minutes(time_string))

def calculate_total_minutes(time_string):
  times = time_string.split(',')

  total_minutes = 0

  for time in times:

    parts = time.split()

    hours = 0
    minutes = 0
    seconds = 0

    for part in parts:
      if 'h' in part:
        hours = int(part[:-1])
      elif 'm' in part:
        minutes += int(part[:-1])
      elif 's' in part:
        seconds += int(part[:-1])

    minutes += seconds // 60
    total_minutes += hours * 60 + minutes

  return total_minutes

time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
print(calculate_total_minutes(time_string))

# The time string is:
# '1h 45m,360s,25m,30m 120s,2h 60s'
# '1h 45m' -> 1 hour = 60 minutes + 45 minutes = 105 minutes
# '360s' -> 360 seconds = 6 minutes
# '25m' -> 25 minutes
# '30m 120s' -> 30 minutes + 120 seconds = 2 minutes = 32 minutes
# '2h 60s' -> 2 hours = 120 minutes + 60 seconds = 1 minute = 121 minutes







