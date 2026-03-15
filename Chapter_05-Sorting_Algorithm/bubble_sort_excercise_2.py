def bubble_sort(L):
    n = len(L)
    
    for i in range(n):
        counter = 0
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                counter += 1
        if counter == 0:
            break
        

if __name__ == "__main__":
    L = [6,1,4,9,2]
    print("Before sort:", L)
    bubble_sort(L)
    print("After sort:", L)

