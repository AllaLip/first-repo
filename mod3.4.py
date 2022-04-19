from pathlib import Path
import json


def register(login, passwd):
    noreg=True
    with open ('id_info.json', 'r') as file:
        data=json.load(file)
    for key in data.keys():
        if key==login:
            noreg=False
    if noreg:
        data[login]=passwd
        with open('id_info.json', 'w') as file:
            json.dump(data, file)
    return noreg
    
   
def login_function(login, passwd):
    reg=False
    with open ('id_info.json', 'r') as file:
        data=json.load(file)
    for l, p in data.items():
        if l==login and p==passwd:
            reg=True
    return reg  
    
users = {'admin': 'admin'}

if Path('id_info.json').exists():
	print('File exists')
else:
	with open('id_info.json','w') as file:
		json.dump(users, file)
		print('File created')

chose=input("For Register chose r \nFor Enter chose e: ")
login=input("Login: ")
passwd=input("Password: ")
if chose=='r':
    if register(login, passwd):
        print("User added")
    else:
        print("User already exist")
elif chose=='e':
    if login_function(login, passwd):
        print("Welcome!")
    else:
        print("Try again")
        









