original = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []
for num in original:
    if num > 5:
        new_array.append(num + 2)

print("Original array:", original)
print("New array:", new_array)
