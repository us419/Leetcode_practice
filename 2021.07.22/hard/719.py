class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def more_pair(guess):
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if more_pair(mid):
                right = mid
            else:
                left = mid + 1

        return left