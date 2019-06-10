import operator
listA = [(1,2), (4,3), (2,10), (12, 5), (6, 7), (9,11), (15, 4)]
print('\n',"sorting using 1st item in the tuple in ascending order")
print(sorted(listA), '\n')
print("sorting using 1st item in the tuple in descending order")
print(sorted(listA, reverse = True),'\n')
print("sorting using 2nd item in the tuple in ascending order")
print(sorted(listA, key = operator.itemgetter(1)), '\n')
print("sorting using 2nd item in the tuple in descending order")
print(sorted(listA, key = operator.itemgetter(1), reverse = True),'\n')