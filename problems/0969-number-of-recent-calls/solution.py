from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        front_t = t - 3000
        while self.q and self.q[0] < front_t:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
