#Accpeted

class Solution:
 def fizzBuzz(self,n:int) -> List[str]:
     numbers = []
     strings = []
     for number in range(1,n+1):
         numbers.append(number)
     for number in numbers:
         if number%3==0 and number%5==0:
            strings.append("FizzBuzz")
         elif number%5==0:
            strings.append("Buzz")
         elif number%3==0:
            strings.append("Fizz")
         else:
            strings.append(str(number))
     return strings
      
