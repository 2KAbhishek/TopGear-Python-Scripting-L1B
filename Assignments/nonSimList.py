#!/usr/bin/env python

def nonSimEle(lst):
    next, finalLst, maxI = 1, [], len(lst) - 1

    for i, v in enumerate(lst):
        next = i+1
        if next > maxI:
            finalLst.append(v)
            break
        if v != lst[next]:
            finalLst.append(v)

    return finalLst


lst1 = [1, 2, 2, 3]
lst2 = [2, 2, 3, 3, 3]

print(lst1, "-->", nonSimEle(lst1))
print(lst2, "-->", nonSimEle(lst2))
