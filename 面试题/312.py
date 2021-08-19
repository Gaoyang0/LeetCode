# https://leetcode-cn.com/problems/burst-balloons/solution/zhe-ge-cai-pu-zi-ji-zai-jia-ye-neng-zuo-guan-jian-/
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        '''
        假设这个区间是个开区间，最左边索引 i，最右边索引 j。 我这里说 “开区间” 的意思是，我们只能戳爆 i 和 j 之间的气球，i 和 j 不要戳
        DP思路是这样的，就先别管前面是怎么戳的，你只要管这个区间最后一个被戳破的是哪个气球，这最后一个被戳爆的气球就是 k
        因为是最后一个被戳爆的，所以它周边没有球了！没有球了！只有这个开区间首尾的 i 和 j 了！！
        这就是为什么DP的状态转移方程是只和 i 和 j 位置的数字有关
        假设 dp[i][j] 表示开区间 (i,j) 内你能拿到的最多金币
        '''
        # dp[i][j] = max(dp[i][k] + val[i]*val[k]*val[j] + dp[k][j]) i<k<j
        # k 是最后一个被戳爆的，所以 (i,j) 区间中 k 两边的东西必然是先各自被戳爆了的，k的左右两边互不干扰

        # 方便计算出入边界
        nums.insert(0, 1)
        nums.insert(len(nums), 1)

        dp = [[0] * (len(nums)) for _ in range(len(nums))]

        def range_best(i, j):
            m = 0
            # k是(i,j)区间内最后一个被戳的气球, k取值在(i,j)开区间中
            for k in range(i + 1, j):
                a = dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                m = max(a, m)
            dp[i][j] = m

        # 对每一个区间长度进行循环
        for step in range(2, len(nums)):
            # 外层的第一次循环相当于dp初始化
            # 对于每一个区间长度，循环区间开头的i
            for i in range(0, len(nums) - step):
                # 计算这个区间的最多金币
                range_best(i, i + step)

        return dp[0][-1]





s = Solution()
print(s.maxCoins([3,1,5,8]))