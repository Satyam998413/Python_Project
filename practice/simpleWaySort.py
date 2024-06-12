# Example usage
arr = ["apple", "banana", "cherry", "date"]

# Sort by length of the string
sorted_by_length = sorted(arr, key=len)
print(sorted_by_length)

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr_desc = sorted(arr, reverse=True)
print(sorted_arr_desc)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            print(i,j)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# def find_second_largest(arr):
#     if len(arr) < 2:
#         return None  # Not enough elements to find the second largest

#     first = second = 0


#     for number in arr:
#         if number > first:
#             second = first
#             first = number
#             print("first",first,second)
#         elif number > second and number != first:
#             second = number
#             print("Sfirst",first,second)

#     print("-------------",first,second)
#     return second if second != float('-inf') else None


str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
