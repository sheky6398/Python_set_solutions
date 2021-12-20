# Add a list of elements to a set
# Given a Python list, Write a program to add all its elements into a given set.

# Given:

# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# Expected output:


# Note: Set is unordered.

# {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}

s1 = {"Yellow", "Orange", "Black"}
s2 = ["Blue", "Green", "Red"]
print(s1.update(s2))
print(s1)

