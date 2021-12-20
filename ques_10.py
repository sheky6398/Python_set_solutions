#  Write a Python program to check if a set is a subset of another set.

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])


print(setx<=sety)
print(setx.issubset(setz))
print(setz.issubset(sety))