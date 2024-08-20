def isPalindrome(x: int) -> bool:
        b = False
        if x < 0 :
            return b
        accum = 0
        copy = x
        while copy >= 1:
            accum = accum + int(copy % 10)
            copy = int(copy / 10)
            accum = accum * 10
        accum = accum / 10
        if (accum == x): 
             b = True
        return b

print(isPalindrome(99))