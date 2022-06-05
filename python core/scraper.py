import requests

print('Input the URL:')
url = input()
r = requests.get(url)
if r.status_code == 200:
    jsoned = r.json()
    try:
        print(jsoned["content"])
    except KeyError:
        print("Invalid quote resource!")
else:
    print("Invalid quote resource!")
