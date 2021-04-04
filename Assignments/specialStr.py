#!/usr/bin/env python

def strCount(tlist):
    sCount = 0
    for ele in tlist:
        if (len(ele) >= 2) and (ele[0] == ele[-1]):
            sCount += 1
    return sCount


list1 = ['axa', 'xyz', 'gg', 'x', 'yyy']
list2 = ['x', 'cd', 'cnc', 'kk']
list3 = ['bab', 'ce', 'cba', 'syanora']

print(strCount(list1))
print(strCount(list2))
print(strCount(list3))
