password=input("Insert password: ")

p=password

while len(p)<=8 or p==p.lower() or p==p.upper():
        p=input("Try again: ")
if len(p)>8:
        print("Acceptable")