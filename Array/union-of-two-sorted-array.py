#1st Approach

def findUnion(arr1, arr2):
    i = 0
    j = 0
    ans = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:

            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])

            i += 1

        elif arr1[i] > arr2[j]:

            if len(ans) == 0 or ans[-1] != arr2[j]:
                ans.append(arr2[j])

            j += 1

        else:

            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])

            i += 1
            j += 1

    while i < len(arr1):

        if len(ans) == 0 or ans[-1] != arr1[i]:
            ans.append(arr1[i])

        i += 1

    while j < len(arr2):

        if len(ans) == 0 or ans[-1] != arr2[j]:
            ans.append(arr2[j])

        j += 1

    return ans


arr1 = [1,2,3,4,5,6,7,8,10,11,11,13,13]
arr2 = [1,2,6,7,8,9,10,12]

print(findUnion(arr1, arr2))