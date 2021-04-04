#!/usr/bin/env python
def tupSort(lst):
    lst.sort(key=lambda x: x[-1])
    return lst


# main program
lst1 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
lst2 = [(1, 3), (3, 2), (2, 1)]

print(tupSort(lst1))
print(tupSort(lst2))
