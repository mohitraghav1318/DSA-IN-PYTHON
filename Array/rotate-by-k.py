#1st Approach 

'''
def leftRotate(arr,k):
    for i in range(k):
        temp = arr[0]
        for j in range(len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = temp
    print(arr)

def rightRotate(arr,k):
    for i in range(k):
        temp = arr[len(arr)-1]
        for j in range(len(arr)-1,0,-1):
            arr[j] = arr[j-1]
        arr[0] = temp
    print(arr)   

arr = [1,3,5,4,5,3,2,7,8]
print(f'Orignal Array : {arr}')
leftRotate(arr,3)
rightRotate(arr,2)       
'''

#2nd Approach  by using reverse algorithm

import dataclasses
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def leftRotate(arr, d):
    n = len(arr)

    d = d % n

    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)

    print("Left Rotate :", arr)


def rightRotate(arr, d):
    n = len(arr)

    d = d % n

    d = n - d

    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)

    print("Right Rotate :", arr)


arr1 = [1, 3, 5, 4, 5, 3, 2, 7, 8]

print("Original Array :", arr1)     

print("enter no of times")
d= int(input())

leftRotate(arr1, d)

rightRotate(arr1, d)   