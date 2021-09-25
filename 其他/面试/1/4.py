from itertools import permutations


def flag(s):
    return True if s == s[::-1] else False

def fun(str1):
    for i in permutations(str1):
        temp = "".join(i)
        if not flag(temp):
            return "YES"
    return "NO"

n = int(input().strip())

for _ in range(n):
    s = input().strip()
    print(fun(s))