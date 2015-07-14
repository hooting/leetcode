#reference to https://leetcode.com/discuss/38206/ac-o-n-solution-in-java-using-buckets-with-explanation
#each element is put into proper bullet, that is:
#the [min, min + t] is put into the 1st bullet
#the [min + t + 1, min + 2t] is put into the 2nd bullet
#and so on.
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0: return False
        minInt = -2147483648
        bullets = dict()
        size = len(nums)
        for i in range(0,size):
            bulletIndex = (nums[i] - minInt) / (t + 1)
            if bullets.has_key(bulletIndex): return True
            if bullets.has_key(bulletIndex - 1):
                if nums[i] - bullets[bulletIndex - 1] <= t: return True
            if bullets.has_key(bulletIndex + 1):
                if bullets[bulletIndex + 1] - nums[i] <= t: return True
            bullets[bulletIndex] = nums[i]
            if len(bullets) > k:
                removeIndex = (nums[i - k] - minInt) / (t + 1)
                del bullets[removeIndex]
        return False