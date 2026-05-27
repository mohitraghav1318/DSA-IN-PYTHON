#1st Approach by remove and append : 

'''
def moveZerosToEnd(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.remove(arr[i])
            arr.append(0)


arr = [0, 1, 0, 3, 12]

moveZerosToEnd(arr)
print(arr)
'''   


#2nd Approach by swaping adjacent 
'''
def moveZerosToEnd(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] == 0:
                arr[j],arr[j+1] = arr[j+1],arr[j] 
    print(arr) 

arr = [0, 1, 0, 3, 12]

moveZerosToEnd(arr)
'''

#3rd Approach using two pointer
'''
def moveZerosToEnd(arr):
    f = 0
    n = 1
    while (f<len(arr) and n<len(arr)):
        if arr[f] == 0 and arr[n] != 0:
            arr[f],arr[n] = arr[n],arr[f]
            f+=1
            n+=1
        elif arr[f] != 0 and arr[n] != 0:
            f+=1
            n+=1
        elif arr[f] == 0 and arr[n] == 0:
            n+=1
    print(arr)   

arr = [0, 1, 0, 3, 0, 0 , 12]

moveZerosToEnd(arr)  
'''
#4th Approach 

def moveZerosToEnd(arr):
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    print(arr)


arr = [2,0, 1, 0, 3, 0, 0, 12]

moveZerosToEnd(arr) 
