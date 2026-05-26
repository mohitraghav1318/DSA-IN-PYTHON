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

#2nd Approach 
