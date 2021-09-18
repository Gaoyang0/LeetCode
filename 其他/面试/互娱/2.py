T = int(input())


def fun(height):
    if len(nums) >=2:
            # res = fun(nums)
            # if nums[0] < nums[1]:
            #     res += 1
            # if nums[-1] < nums[-2]:
            #     res += 1
        p = 0
        stack = []
        res = 0
        cur = height[0]
        while p < len(height):

            while len(stack) > 0 and height[p] > height[stack[-1]]:
                temp = stack.pop()
                if len(stack) == 0:
                    break

                h = min(height[p], height[stack[-1]]-height[temp])
                if h>=cur:
                    res += 1
                    cur = h

            stack.append(p)
            p += 1
        return res
    else:

        return 0



for _ in range(T):
    a, b = map(int, input().strip().split(" "))
    nums = list(map(int, input().strip().split(" ")))
    if len(nums) >=2:
        b = b-1
        res = 0
        p = b - 1
        while p >= 0 and nums[p]<nums[b]:
            p -= 1

        res += fun(nums[:p])

        p = b +1
        while p <len(nums) and nums[p]<nums[b]:
            p += 1
        res += fun(nums[:p])
        res += fun(nums[p:])


        print(res+1)
    else:
        print(0)
