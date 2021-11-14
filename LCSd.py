from cProfile import Profile
from pstats import Stats
import sys
prof = Profile()
prof.disable()
import random
import string

def LCSd(first, second):
    m = len(first)
    n = len(second)
    if m == 0 or n == 0:
       return ""
    matrix = [[0 for x in range(n + 1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif first[i-1] == second[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix])) 

    index = matrix[m][n]
    sub_array = [''] * (index)
    i = m
    j = n
    while i > 0 and j > 0:
        if first[i-1] == second[j-1]:
            sub_array[index-1] = first[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1

    result = "".join(sub_array)
    return result

def rand_string(size, chars):
    return ''.join(random.choice(chars) for x in range(size))

size = 10
first = rand_string(size, string.ascii_letters)
second = rand_string(size, string.ascii_letters)
prof.enable()
sub = LCSd(first, second)
prof.disable()
prof.dump_stats("LCSdy.stats")
with open('LCSd10.txt', 'a') as output:
    output.write("Test:  two random strings of size: " + str(size) + '\n')
    stats = Stats('LCSdy.stats', stream=output)
    stats.sort_stats('time')
    stats.print_stats()

print("First: " + first)
print("Second: " + second)
print("LCS: " + str(sub))



