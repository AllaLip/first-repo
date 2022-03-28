a=int(input('Insert a: '))
b=int(input('Insert b: '))
c=int(input('Insert c: '))
if a==b and a==c:
        print(3)
elif a==b or b==c or a==c:
        print(2)
else:
        print(0)
