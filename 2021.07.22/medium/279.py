class Solution:
    def numSquares(self, n: int) -> int:        
#         dp = [1e9] * (n+1)
#         dp[0] = 0
#         for i in range(1, n+1):
#             j = 1
#             while j**2 <= i:
#                 x = j**2
#                 dp[i] = min(dp[i], dp[i-x]+1)
#                 j += 1
                
        # return dp[n]
        
        arr = [i for i in range(n + 1)]
        for i in range(1,n + 1):
            j = 1
            while j * j <= i:
                arr[i] = min(arr[i],arr[i - (j * j)] + 1)
                j += 1
        return arr[-1]
