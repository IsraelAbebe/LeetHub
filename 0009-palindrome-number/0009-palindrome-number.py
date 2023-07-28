class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        # if len(x) %2 != 0:
        #     return False
        counter = 0
        while counter < len(x):
            # print( x[counter], x[len(x)-1-counter])
            if x[counter] == x[len(x)-counter-1]:
                counter += 1
            else:
                return False
        return True
