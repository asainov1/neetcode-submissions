from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i in range(len(tickets)):
            queue.append((tickets[i], i))
        cnt = 0
        while queue:
            ticketToBuy, index = queue.popleft()
            if k == index and ticketToBuy == 1:
                return cnt + 1

            if ticketToBuy > 1:
                queue.append((ticketToBuy - 1,index)) #2-1 , 
                cnt += 1
            else:
                cnt += 1

#ticketToBuy, index = queue.popleft()

        
