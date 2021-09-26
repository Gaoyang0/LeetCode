class Solution:
    def pathAvailable(self , matrix , starts , ends ):
        # write code here
        res = []
        n = len(matrix)
        m = len(matrix[0])
        def fun(start, end):
            visited = set()

            visited.add(start)
            que = [start]
            while len(que) > 0:
                cnt = len(que)
                for _ in range(cnt):
                    a, b = que.pop(0)
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        temp_x, temp_y = a+x, b+y
                        if 0 <= temp_x < n and 0 <= temp_y < m and matrix[temp_x][temp_y] == 1 and (temp_x, temp_y) not in visited:
                            if temp_x == end[0] and temp_y == end[1]:
                                return True
                            que.append((temp_x, temp_y))
                            visited.add((temp_x, temp_y))
            return False


        for s, e in zip(starts, ends):
            res.append(fun((s[0], s[1]), (e[0], e[1])))
        return res




s = Solution()
print(s.pathAvailable([ [1,1,1,1], [0,0,0,0], [1,1,1,1], [1,1,0,1] ],[[0,0],[0,1],[2,0]],[[0,3],[2,2],[3,3]]))