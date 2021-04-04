#!/usr/bin/env python
def reachNumber(target):
    target = abs(target)
    k = 0
    while target > 0:
        k += 1
        target -= k

    return k if target % 2 == 0 else k + 1 + k % 2


print('1000000000 can be reached in', reachNumber(1000000000), 'steps.')
print('-1000000000 can be reached in', reachNumber(-1000000000), 'steps.')
