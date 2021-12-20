# Write a Python program to create set difference.

setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])

diff1 = set(setc1)-set(setc2)
diff2 = set(setc2)-set(setc1)
print(diff1)
print(diff2)

#Another method
print(setc1.difference(setc2))
print(setc2.difference(setc1))