# PayPay Corp invited you to take PayPay Corp - QA Coding Challenge on CodeSignal

# Write a function returning a sum of digits of "n" which has two digits
def solution(n):
    str_n = str(n)
    str_a = str_n[0]
    str_b = str_n[1]
    if not (0 <= int(str_a) <= 9 and 0 <= int(str_b) <= 9):
        raise ValueError("Both nums must be single digits")

    return int(str_a) + int(str_b)

print(solution(21))

# Quiz. What is the next number in the following sequence?
# 1, 1, 2, 3, 5, 8, 13, *
# A: 21

# What happens when user asks the browser
# A:
# 1. URL parsing;
# 2. DNS lookup;
# 3. Request heats loadbalancer of the site;
# 4. HTTP/S request procesed by the web server;
# 5. Responce (200 if success) and data transfer (HTML returned to the browser);
# 6. Page rendering in the browser;
# 7. JavaScript execution;
# 8. Page displayed in the browser;
# 9. User interacts with a dynamic page and JavaScript updates the page;


