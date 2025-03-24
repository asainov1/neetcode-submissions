class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []
        for birth, death in logs:
            events.append((birth, 1))
            events.append((death , -1))
        events.sort()
        mx = 0
        curr = 0 
        earliest_year = 0
        for year, change in events:
            curr += change 
            if curr > mx:
                mx = curr
                earliest_year = year
        return earliest_year
