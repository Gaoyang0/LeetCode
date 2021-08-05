from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 这样可以使x[0]升序, x[1]降序, x[0]优先级更大
        people.sort(key=lambda x: (x[0], -x[1]))

        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            # 前面必须有person[1]个空位置+自己要占一个空位置
            spaces = person[1] + 1
            for i in range(n):
                # 判断位置是否为空
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans


s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))