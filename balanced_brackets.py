

def is_balanced(str1):
    open = ["(", "{", "["]
    close = [")", "}", "]"]
    s = []
    for i in str1:
        if i in open:
            s.append(i)
        elif i in close:
            pos = close.index(i)
            if (s[len(s)-1] == open[pos]):
                s.pop()
            else:
                return False

    if len(s) > 0:
        return False
    else:
        return True


str1 = "({}[])"
print(is_balanced(str1))