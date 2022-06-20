import requests

r=requests.get('https://www.cnn.com/2022/05/27/business/elon-musk-billionaires-tweet/index.html')

if 300 >= r.status_code >= 200:
    print(f"\nPASS_STATUS = {r.status_code}")
else:
    print(f'\nFAIL_STATUS ="{r.status_code}"')
print(f'\nReceived responce = "{r}"')
x1 = r.text
wrd = 'war'
# print(x1)
if wrd in x1:
    print(f'\nFound: "{wrd}"')
else:
    print (f'\nNot found: "{wrd}"')