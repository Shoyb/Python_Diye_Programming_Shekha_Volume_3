def is_balanced(input_str):
    s = list()
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    for i in input_str:
        if i in opening:
            s.append(i)
        
        for j in range(3):
            if not s:
                return False
            if s[-1] == opening[j] and i == closing[j]:
                s.pop()
                break
    return not s

if __name__ == "__main__":
    input_str = input()
    if is_balanced(input_str):
        print(input_str, "is balanced")
    else:
        print(input_str, "is not balanced")