
def binarySearch(numbers, find):
    if len(numbers) < 0:
        print("Too Small")
    
    low = 0
    high = len(numbers)
    #mid = (low+high)//2

    while low<=high:
        mid = (low+high)//2
        if numbers[mid] == find:
            return mid
        elif numbers[mid] > find:
            high = mid-1
        elif numbers[mid] < find:
            low = mid+1
    
    return -1

def main():
    numbers = [1,2,3,4,6,8,9]
    find = 6
    if binarySearch(numbers, find) == -1:
        print("Could not find the value")
    else:
        print("Found it")

main()
