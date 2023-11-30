class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
 
        
        boat = 0
        people.sort()
        left, right = 0 , len(people)-1
        while left <= right:
            if people[left] + people[right] == limit:
                boat += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                boat += 1
                right -=1
            elif left == right:
                boat += 1
                left += 2
            else:
                boat += 1
                left += 1
                right -=1

        return boat
