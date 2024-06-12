# Given array
a = [1, 22, 33, 44, 44, 44, 55, 55, 55]

# Step 1: Initialize an empty dictionary to store counts
counts = {}

# Step 2: Iterate through the array and update counts
for num in a:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

# Print counts of each element
print("Counts of each element:", counts)

# Step 3: Filter out duplicates
duplicates = {}
for key, value in counts.items():
    if value > 1:
        duplicates[key] = value

# Print only duplicates
print("Duplicate elements and their counts:", duplicates)