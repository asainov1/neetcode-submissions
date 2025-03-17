class Solution:
    def calPoints(self, operations: List[str]) -> int:
        needed_dict = ["+","D","C"]
        result = []
        for op in range(len(operations)):
            if operations[op] not in needed_dict:
                result.append(int(operations[op]))
            else:
                if operations[op] == "C":
                    result.pop()
                elif operations[op] == "D":
                    result.append(2 * int(result[-1])) 
                else:
                    result.append(int(result[-1]) + int(result[-2]))
        print (result)
        return sum(result)
