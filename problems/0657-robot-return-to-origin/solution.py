class Solution:
    def judgeCircle(self, moves: str) -> bool:
        starting = [0, 0]
        checker = {"U":1, "L":1, "R":-1, "D":-1}
        for move in moves:
            if move == "U" or move == "D":
                starting[0] += checker[move]
            else:
                starting[1] += checker[move]
        if starting == [0,0]:
            return True
        return False
