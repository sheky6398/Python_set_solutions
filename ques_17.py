#  Write a Python program to remove the intersection of a 2nd set from the 1st set.

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print(sn1.difference_update(sn2))
print(sn1)
print(sn2.difference_update(sn1))
print(sn2)
