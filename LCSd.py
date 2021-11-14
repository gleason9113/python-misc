

def LCSd(first, second):
    first_len = len(first)
    sec_len = len(second)
    if first_len == 0 or sec_len == 0:
        return 0 #One or both strings is empty
    matrix = [[0 for x in range(sec_len + 1)] for x in range(0, first_len + 1)]
    for i in range(0, first_len + 1):
        for j in range(0, sec_len + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif first[i-1] == second[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1]) 
    index = matrix[first_len][sec_len]
    sub = [""] * (index+1) 
    while i > 0 and j > 0:
        if first[i-1] == second[j-1]:
            sub[index-1] = first[index-1]
            i -= 1
            j -= 1
            index -= 1
        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    result = "".join(sub)
    return result

first = "abracadabra"
second = "mkjlyycadazyxl"
sub = LCSd(first, second)
print("LCS: " + str(sub))


