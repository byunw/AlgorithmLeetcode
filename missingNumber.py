
# my solution for one of the problems in blind75. 
#The goal was to solve this problem and make the habit of solving 1 leetcode problem per day.
class Solution:
  def missingNumber(self,nums: List[int]) -> int:
      n = len(nums)
      for number in range(0,n+1):
          if(number not in nums):
             return number
