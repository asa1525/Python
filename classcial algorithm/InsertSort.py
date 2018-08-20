# 1
'''
def insertsort(l):
    for i in range(1, len(l)):
        print(l[:i])
        for j in range(len(l[:i])):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]

if __name__ == "__main__":
    nums = [2, 6, 8, 5, 1, 4, 9, 3, 7]
    print(nums)
    insertsort(nums)
    print("result: ", str(nums))
'''

# 2
'''
def insertSort(arr):
    length = len(arr)
    for i in range(1, length):
        x = arr[i]
        for j in range(i, -1, -1):
            if x < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                break
        arr[j] = x

def printArr(arr):
    for item in arr:
        print(item)
arr = [2, 6, 8, 5, 1, 4, 9, 3, 7]
insertSort(arr)
printArr(arr)
'''

# 3
