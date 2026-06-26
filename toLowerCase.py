#Type: string
#Difficulty: Easy
#Used Language: Python
#Accepted Answer
class Solution:
  def toLowerCase(self,s: str)-> str:
      final_answer = []
      for c in s:
          if(c.isupper()):
             final_answer.append(c.lower())
          else:
             final.answer.append(c)
      result = "".join(final_answer)
      return result
           
    
