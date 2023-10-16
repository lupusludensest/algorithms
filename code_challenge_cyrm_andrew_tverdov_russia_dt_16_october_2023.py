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