def f_common (list1, list2):
    return list(set(list1) & set(list2))


list1 = [2, 5, 9, 7, 3]
list2 = [2, 5, 7, 8, 10, 1]

common = f_common(list1, list2)
print("Common numbers between two list:",common)