def getSum(h):
    sum1 = 0
    for i in h:
        sum1 = sum1 + i
    return sum1


def equalStacks(h1, h2, h3):
    sum1 = getSum(h1)
    sum2 = getSum(h2)
    sum3 = getSum(h3)
    mini = min(sum1, sum2, sum3)
    while True:
        if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
            return 0
        if sum1 > mini:
            h1.pop(0)
        if sum2 > mini:
            h2.pop(0)
        if sum3 > mini:
            h3.pop(0)
        sum1 = getSum(h1)
        sum2 = getSum(h2)
        sum3 = getSum(h3)
        mini2 = min(sum1, sum2, sum3)
        if mini2 == mini and sum1 == sum2 and sum1 == sum3:
            return mini
        else:
            mini = mini2

h1 = [1, 1, 1, 1, 2]
h2 = [3, 7]
h3 = [1, 3, 1]
print(equalStacks(h1, h2, h3))
