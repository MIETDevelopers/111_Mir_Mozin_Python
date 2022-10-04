#Linear search
def LinearSearch(input_list: list, element: int):
    list_len = len(input_list)
    for i in range(list_len):
        if input_list[i] == element:
            return i
    return -1

myList = [1, 23, 45, 23, 34, 56, 12, 45, 67, 24]
print("Given list is:", myList)
position = LinearSearch(myList, 12)
print("Element 12 is at position:", position)


#Binary Search

def binary_search(arr, a, low, high):
    # Repeat until low and high meet each other
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == a:
            return mid
        elif arr[mid] < a:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 2, 3, 4, 5, 6, 7]
a = 4

print("The given array is", arr)

print("Element to be found is ", a)

index = binary_search(arr, a, 0, len(arr)-1)
if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")
