def selectsort(l):
    length = len(l) - 1

    while length:
        index = length # index = 5
        for j in range(length):
            if l[j] > l[index]: # l[2] > l[5]:
                index = j # index = 2
        l[length], l[index] = l[index], l[length] # l[length], l[index] = 9, 7
        print(l[length], l[index])
        print(len(l) - length, l)
        length -= 1

if __name__ == "__main__":
    l = [5, 1, 9, 3, 2, 7]
    print(l)
    selectsort(l)
    print("result: " + str(l))