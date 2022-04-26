def binary_search(arr, n):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if arr[mid]<n:
            low=mid+1
        elif arr[mid]>n:
            high=mid-1
        else:
            return mid
    return -1

arr=[2, 5, 10, 14, 19, 24, 28, 33, 41]
n=int(input('insert element: '))
r=binary_search(arr, n)
if r!=-1:
    print("Элемент под индексом ", str(r))
else:
    print("Элемента нет в списке")
