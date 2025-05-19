class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = {"a","e","i","o","u","A","E","I","O","U"}
        chars = list(s)
        left = 0
        right = len(chars) - 1
        while left<right:
            while left<right and chars[left] not in VOWELS:
                left +=1
            while left<right and chars[right] not in VOWELS:
                right -=1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -=1
        return "".join(chars)