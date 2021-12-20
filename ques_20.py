#  Remove items from set1 that are not common to both set1 and set2
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:

# {40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))