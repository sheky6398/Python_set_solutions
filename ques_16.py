# Write a Python program to check if a given set is superset of itself and superset of another given set.

nums = {10,20,30,40,50}
print("Original set: ",nums)
print("If nums is superset of itself?")
print(nums.issuperset(nums))
num1 = {1, 2, 3, 4, 5, 7}
num2 = {2, 4}
num3 = {2, 4}
print(num1.issuperset(num2))
print(num1>num2)
print(num2>num3)