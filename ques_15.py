# Write a Python program to check if two given sets have no elements in common.

x = {1,2,3,4}
y = {4,5,6,7}
z = {8}
print(x.isdisjoint(y))
print(x.isdisjoint(z))
print(y.isdisjoint(x))