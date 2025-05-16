class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_now=max(candies)
        result=[]
        for current in candies:
            can_be_best = (current+extraCandies) >= max_now
            result.append(can_be_best)
        return result