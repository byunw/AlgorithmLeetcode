#Type: string
#Language used: python
#Difficulty: easy
#Accepted Answer
class Solution:
  def lengthOfLastWord(self,s:str)->int:
      words = s.split()
      return len(words[-1])

