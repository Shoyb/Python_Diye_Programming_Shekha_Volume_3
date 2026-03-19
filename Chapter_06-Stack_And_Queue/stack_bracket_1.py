def is_balanced(input_str):
    s = list()
    
    for i in input_str:
        if i == "(":
            s.append(i)
        if i == ")":
            if not s:
                return False
            s.pop()
    return not s

if __name__ == "__main__":
    input_str = input()
    if is_balanced(input_str):
        print(input_str, "is balanced")
    else:
        print(input_str, "is not balanced")