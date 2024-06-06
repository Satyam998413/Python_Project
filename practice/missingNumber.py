def find_missing_number(arr):
    n = len(arr) + 1  # since one number is missing, the array length is n-1
    sum_expected = n * (n + 1) // 2
    sum_actual = sum(arr)
    missing_number = sum_expected - sum_actual
    return missing_number

# Example usage:
array = [1, 3, 4, 5, 6,7]  # Example array where 3 is missing
missing_number = find_missing_number(array)
print(f"The missing number is: {missing_number}")