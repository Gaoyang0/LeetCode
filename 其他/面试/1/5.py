

def fun(str1):
    res = ""
    dict_num = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    i = 0
    while i <len(str1):
        if str1[i] == "0":
            res += "-"
        if str1[i] == "-":
            count = 0
            while i+1<len(str1) and str1[i] == str1[i+1]:
                i += 1
                count += 1
            count +=1
            if count >=2:
                continue
            else:
                res = res[:-1]
                i = i - 1
                str1 = str1[:i+1] + "_" +
                i += 1
                continue

        if 2<=int(str1[i])<=9:
            ll = dict_num[str1[i]]
            count = 0
            while i+1<len(str1) and str1[i] == str1[i+1]:
                i += 1
                count += 1
            index = count % len(ll)
            res += ll[index]

        i += 1
    print(res)

# fun("2--2-2---222--2")

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    s = input().strip()
    fun(s)
