def shellsort(nums):
    step = len(nums)//2
    while step > 0:
        for i in range(step, len(nums)):
            while i >= step and nums[i-step] > nums[i]:
                nums[i], nums[i-step] = nums[i-step], nums[i]
                i -= step
        step = step//2
    return nums

if __name__ == "__main__":
    nums = [4, 9, 5 ,3 ,6 ,2 ,7, 1]
    print(shellsort(nums))