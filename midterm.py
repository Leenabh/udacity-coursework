
# function to find the minimum and maximum when two additional variables are allowed.
def findminmax(numbers):
    min = numbers[0]
    max = numbers[0]

    for n in numbers:
        if n > max:
            max = n
        if n < min:
            min = n
    
    print("Min: {} Ma: {}".format(min, max))

# function to sort an array in O(n) time when memory is not a contraint. 
def sortnarray(numbers):
    temp = [0] * 100

    for n in numbers:
        temp[n] += 1
    
    num_pointer = 0
    for i in range(len(temp)):
        n = temp[i]
        while n > 0:
            numbers[num_pointer] = i
            num_pointer += 1
            n -= 1
    return numbers

print(sortnarray([0, 1,3,2, 5, 4, 99, 5,6]))