import requests

payload = {
    'form': {
        'key1': 'value1',
        'key2': 'value2'
    },
}
r = requests.post('https://httpbin.org/post', payload)

print(r.text)

if 300 >= r.status_code >= 200:
    print(f"PASS_STATUS = {r.status_code}")
else:
    print(f'\nFAIL_STATUS ="{r.status_code}"')
