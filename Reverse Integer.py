#this seems not to be the approach

# Now the question is, how do we know that we've reached the half of the number?

# Since we divided the number by 10, and multiplied the reversed number by 10, when the original number is less than the reversed number, it means we've processed half of the number digits.

import math
class Solution:
    def reverse(self, x: int) -> int:
        ran = [-1*pow(2,31),pow(2,31)-1]
        
        y=abs(x)
        x = -1 if x<0 else 1
        y=int("".join(list(str(y))[::-1]))
        y*=x
        if(y<ran[0] or y>ran[1]):
            return 0
        return y