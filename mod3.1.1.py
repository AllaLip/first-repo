x=int(input("Insert x: "))
p=int(input("Insert percent: "))
y=int(input("Insert y: "))

years=0

while x<y:
	yearly=x*(p/100)
	x=x+yearly
	years+=1

print(years)
