from array import array

arr = array('i', [13, 7, 10, 11])
print(arr)

# Traverse
for i in arr:
    print(i)

# Insert
arr.insert(1, 6)
print(arr)

# Access
print(arr[0])

# Update
arr[0] = 12
print(arr)

# Remove/Delete
arr.remove(7)
print(arr)