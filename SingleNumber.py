#current goal: pass my solution to get into the habit of solving at least 1 leetcode problem a day which will help me pass an OA which can be a part of getting a ml engineer job.
#status: current goal was acheived today.

#Accepted Solution
from collections import Counter
class Solution:
  def singleNumber(self,nums: List[int]) -> int:
      frequency = Counter(nums)
      for integer in frequency:
          for integer in frequency:
              if(frequency[integer]==1):
                 return integer
                
