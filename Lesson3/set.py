my_set = {1,2,3}

my_set = set([4, 5 ,6])

my_set = set()

my_set = {1, 2, 2, 3, 3, 3}

print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set_method = set1.union(set2)
union_set_operator = set1 | set2

print("Rezultati i union i 2 set me method:", union_set_method)
print("Rezultati i union i 2 set me operator:", union_set_operator)

intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2

print("Rezultati i intersection i 2 set me method:", intersection_result_method)
print("Rezultati i intersecttion i 2 set me operator:", intersection_result_operator)

difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print("Resultati i difference i 2 set me method:", difference_result_method)
print("Resultati i difference i 2 set me operator:", difference_result_operator)

symmetric_difference_method = set1.symmetric_difference(set2)
symmetric_difference_operator = set1 ^ set2

print("Resultati i symmetric difference i 2 set me method:", symmetric_difference_method)
print("Resultati i symmetric difference i 2 set me operator:", symmetric_difference_operator)

my_set = {1, 2 ,3}

my_set.add(7)

my_set.remove(3)

my_set.discard(8)

print(my_set)

my_set.clear()