from typing import List
from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = Counter(nums)
        for i in c:
            if(target - i in c):
                if(target-i != i):
                    return [nums.index(i),nums.index(target-i)]
                elif(c[i]>1):
                    return [j for j,val in enumerate(nums) if val==i]
        
sol = Solution()
print(sol.twoSum([1,3,3],6))
