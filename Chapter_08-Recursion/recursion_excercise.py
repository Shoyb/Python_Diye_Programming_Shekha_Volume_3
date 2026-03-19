def print_number_1(n):
    if n == 0:
        return
    print(n)
    print_number_1(n-1)

def print_number_2(n):
    if n == 0:
        return
    print_number_2(n-1)
    print(n)

if __name__ == "__main__":
    print("Function 1:")
    print_number_1(5)
    print("Function 2:")
    print_number_2(5)