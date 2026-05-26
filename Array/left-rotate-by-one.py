#1st approach

'''
arr1 = [1,2,3,4,4,5,6,7,7,8]
arr2 = []

for i in range(1, len(arr1)):
    arr2.append(arr1[i])
arr2.append(arr1[0])
print(arr2)
'''


#2nd approach

arr1 = [1,2,3,4,4,5,6,7,7,8]

temp = arr1[0]
for i in range(len(arr1)-1):
    arr1[i] = arr1[i+1]
arr1[len(arr1)-1] = temp
print(arr1)

