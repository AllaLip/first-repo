list1=[1, 4, 1, 6, 'hello', 'a', 5, 'hello', 4]
x=set(list1)
list_dup=[]

for i in x:
        if list1.count(i)>1:
                list_dup.append(i)
print(list_dup)
