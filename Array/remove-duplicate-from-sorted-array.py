arr = list(map(int, input().split() ))
i = 0
j = 1
while j < len(arr):
    if arr[i] != arr[j]:
        i += 1
        j += 1
    else:
        print("Duplicate element: ", arr[j])
        arr.pop(j)
print("Array after removing duplicates: ", arr)