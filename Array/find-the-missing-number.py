#1st Approach 


# def missingNumber(arr, N):

#     hashArr = [0] * (N + 1)

#     for num in arr:
#         hashArr[num] = 1

#     for i in range(1, N + 1):

#         if hashArr[i] == 0:
#             return i


#2nd Approach

def missingNumber(arr, N):

    expected = (N * (N + 1)) // 2

    actual = sum(arr)

    return expected - actual

arr = [1,2,3,4,5,6,8]
n = 8
print(missingNumber(arr,8))