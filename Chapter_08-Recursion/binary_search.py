def binary_search(L, x, left, right):
    if left > right:
        return -1
    mid = (left+right) // 2
    
    if L[mid] == x:
        return mid
    if L[mid] < x:
        return binary_search(L, x, mid+1, right)
    elif L[mid] > x:
        return binary_search(L,x, left, mid-1)
    
if __name__ == "__main__":
    L = [1,2,3,5,6,7,8,9]
    left = 0
    right = len(L) - 1
    
    for x in range(1,11):
        position = binary_search(L,x, left, right)
        
        if position == -1:
            if x in L:
                print(x, "is in L, but function returned -1")
            else:
                print(x, "is not in L")
        else:
            if L[position] == x:
                print(x, "found in correct position.")
            else:
                print("binary search returned", position, "for", x, "which is incorrect")
    print("Program terminated.")