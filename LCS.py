from cProfile import Profile
from pstats import Stats
import sys
prof = Profile()
prof.disable()
import math
import random
import string

def lcs(first, second):
    if len(first) == 0 or len(second) == 0:
        return ""
    elif first[0] == second[0]:
        return first[0] + lcs(first[1:], second[1:])
    else:
        sub1 = lcs(first[1:], second)
        sub2 = lcs(first, second[1:])
        if len(sub1) > len(sub2):
            return sub1
        else:
            return sub2

def rand_string(size, chars):
    return ''.join(random.choice(chars) for x in range(size))

size = 25
first = rand_string(size, string.ascii_letters)
second = rand_string(size, string.ascii_letters)
prof.enable()
sub = lcs(first, second)
prof.disable()
prof.dump_stats("LCSnaive.stats")
with open('LCSn25 .txt', 'a') as output:
    output.write("Test:  two random strings of size: " + str(size) + '\n')
    stats = Stats('LCSnaive.stats', stream=output)
    stats.sort_stats('time')
    stats.print_stats()

print("First: " + first)
print("Second: " + second)
print("LCS: " + str(sub))