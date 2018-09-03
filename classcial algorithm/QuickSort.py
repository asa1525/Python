# 1
'''
def quicksort(num, start, end):
    i = start
    j = end

    if i >= j:  
        return False

    key = num[i]

    while i < j:
        while i < j and key <= num[j]:
            print(key, num[j], '*'*30)
            j -= 1
        num[i] = num[j]

        while i < j and key > num[i]:
            print(key, num[i], '*'*30)
            i += 1
        num[j] = num[i]

    nums[i] = key

    quicksort(num, start, i-1)
    quicksort(num, i+ 1, end)

if __name__ == "__main__":
    nums = [2, 6, 8, 5 , 1, 4, 9, 3, 7]
    quicksort(nums, 0, len(nums)-1)
    print('result:', nums)
'''

# 2
#quick_sort_2 = lambda array: array if len(array) <= 1 else quick_sort_2([item for item in array[1:] if item <= array[0]]) + [array[0] + quick_sort_2([item for item in array[1:] if item > array [0]])

#if __name__ == "__main__":
    #print(quick_sort_2([2, 6, 8, 5 , 1, 4, 9, 3, 7]))


# 3
def quick_sort_3(array, left, right):
    if left >= right:
        return
    low = left # low = 0
    high = right # high = 8
    key = array[low] # key = 2
    print('low,high,key:', low, high, key)
    while left < right: # while 0 < 8 :
        while left < right and array[right] > key:  # while 0 < 8 &  7 > 2
            right -= 1                              # right = 4
        array[left] = array[right]                  # array[left] = 1
        print('array[left]',array[left], 'array[right]:', array[right])

        while left < right and array[left] <= key:  # 3 < 7 & 5 <= 2 !X
            left += 1
        array[right] = array[left]                  # array[right] = 3
        print('array[right]',array[right], 'array[left]:', array[left])

    array[right] = key
    print('array[right]:', array[right])

    quick_sort_3(array, low, left - 1)
    quick_sort_3(array, left + 1, high)

if __name__ == "__main__":
    nums = [2, 6, 8, 5, 1, 4, 9, 3, 7]
    quick_sort_3(nums, 0, len(nums) - 1)
    print('results: ', nums)