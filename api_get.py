import requests

r=requests.get('https://www.cnn.com/2022/05/27/business/elon-musk-billionaires-tweet/index.html')

if 300 >= r.status_code >= 200:
    print(f"PASS_STATUS = {r.status_code}")
else:
    print(f'\nFAIL_STATUS ="{r.status_code}"')

whole_txt = r.text
wrd = 'war'
# print(whole_txt)
if wrd in whole_txt:
    print(f'\nFound: "{wrd}"')
else:
    print (f'\nNot found: "{wrd}"')