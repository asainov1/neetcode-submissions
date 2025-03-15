class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        res = 0
        checker = {"++X":'+1', "--X":'-1',"X++":'+1', "X--":'-1'}
        for operation in operations:
            performed = x + eval(checker[operation])
            res += performed
        return res
