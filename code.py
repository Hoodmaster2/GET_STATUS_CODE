import requests
print('start your link with https:// or http://')
l = input('enter link: ')

x = requests.get(l)
y = x.status_code

if y == 200:
    print('SUCCESS')
else:
    print('FAILED!')
