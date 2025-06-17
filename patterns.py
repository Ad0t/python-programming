# n = int(input())
n = 4

def sq_pat(n):
    for i in range(n):
        for j in range(n):
            print("*", end="\t")
        print("\n")

def tri_pat1(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="\t")
        print("\n")

def tri_pat2(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="\t")
        print("\n")


for i in range(n):
    for j in range(n-i-1):
        print(" ", end="\t")
    for j in range(i+1):
        print("*", end="\t")
    print("\n")
print("-"*30)

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="\t")
    for j in range(i+1):
        print("*", end="\t")
    # print("\n")
    for j in range(i):
        print("*", end="\t")
    print("\n")
print("-"*30)

