#!/usr/bin/env python
def xSort(lst):
    xLst = []
    nonXlst = []
    for ele in lst:
        if ele[0].lower() == "x":
            xLst.append(ele)
        else:
            nonXlst.append(ele)
    xLst.sort(), nonXlst.sort()
    return xLst + nonXlst


lst1 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
lst2 = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']

print(lst1, " -> ", xSort(lst1))
print(lst2, " -> ", xSort(lst2))
