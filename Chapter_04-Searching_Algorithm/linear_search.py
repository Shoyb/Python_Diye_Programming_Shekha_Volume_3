def linear_search(L,x):
    for i in range(len(L)):
        if L[i] == x:
            return i
    return -1