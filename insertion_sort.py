def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1]=arr[j-1], arr[j]
            else:
                break

arr=[-2, 4, 0, -6, 1, 10, 5, 14, 7, -8, 3]
insertion_sort(arr)
print(arr)

            
