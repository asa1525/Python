def bubblesort(l):
    length = len(l) - 1
    for i in range(1, length):
        for j in range(len(l) - i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

if __name__ == "__main__":
    nums = [2, 6, 8, 5, 1, 4, 9, 3, 7]
    print('Result: ', bubblesort(nums))