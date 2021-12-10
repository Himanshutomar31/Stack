# Enter your code here. Read input from STDIN. Print output to STDOUT
no_of_oper = int(input().strip())
s = ""
stack = []
for i in range(no_of_oper):
    lst = list(input().strip().split(" "))
    opr = lst[0]
    if opr == "1":
        stack.append(s)
        s = s + str(lst[1])
    elif opr == "2":
        stack.append(s)
        s = s[0:len(s) - int(lst[1])]
    elif opr == "3":
        print(s[int(lst[1]) - 1])
    else:
        s = stack.pop()







