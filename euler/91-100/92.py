known = {}
def squareDigitSum(n):
    if n == 1:
        return False
    elif n == 89:
        return True
    if str(n) in known:
        return known[str(n)]
    else:
        total = 0
        for num in str(n):
            total += int(num) * int(num)
        result = squareDigitSum(total)
        known[str(n)] = result
        return result

total = 0
for i in range(1,10000000):
    if squareDigitSum(i):
        total += 1
    if i % 100000 == 0:
        print(i)
print(total)
