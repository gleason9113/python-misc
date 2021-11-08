#Implementation of rod-cutting algorithm with profiling

from cProfile import Profile
from pstats import Stats
import sys
prof = Profile()

prof.disable()
import math
import random

def rod_cut(prices, v, n):
    for i in range(1, n + 1):
        m_v = -1000
        for j in range(0, i):
            temp = prices[j] + v[i - j - 1]
            m_v = max(m_v, temp)
        v[i] = m_v

    return v

rod = 60000   
prices = []
prices.append(1)
for i in range(0, rod):
    a = random.randint(0, 6)
    prices.append(prices[-1] + a)

n = len(prices)
v = [0 for x in range(n+1)]
v[0] = 0

prof.enable()
rod_cut(prices, v, n)
prof.disable()
prof.dump_stats("rod_cut.stats")
with open('output.txt', 'a') as output:
    output.write("Test:  array size " + str(rod) + " elements.")
    stats = Stats('rod_cut.stats', stream=output)
    stats.sort_stats('time')
    stats.print_stats()

print("Max value: " + str(v[n]))