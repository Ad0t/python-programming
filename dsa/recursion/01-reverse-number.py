# i = int(input("Number: "))
def reverseNumberIteration (i):
    c = 0
    while i > 0:
        r = i % 10
        c = c * 10 + r
        i = i // 10
    return c
# y = reverseNumberIteration (i)
# print(y)

def reverseNumberRecursion (i):
    if i < 10:
        return i
    nd = len(str(i))-1
    r = i % 10
    return r*(10**nd) + (reverseNumberRecursion(i // 10))
x = reverseNumberRecursion(98765)
print(x)
    