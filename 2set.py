a = {1, 2, 3, 4,5} 
b = {4, 5, 6, 7, 8}

print("a:", a)
print("b:", b)

print("Elements of a:")
for element in a:
    print(element)

union_set = a.union(b)
print("Union of a and b:", union_set)

intersection_set = a.intersection(b)
print("Intersection of Set 1 and Set 2:", intersection_set)

difference_set = a.difference(b)
print("Difference of a and b (a - b):", difference_set)