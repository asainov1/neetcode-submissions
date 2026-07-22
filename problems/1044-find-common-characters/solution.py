from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter1 = Counter(words[0])

        for i in range(1, len(words)):
            counter_curr = Counter(words[i])

            for k in counter1:
                counter1[k] = min(counter1[k], counter_curr[k])
        result = []
        for k, v in counter1.items():
            for _ in range(v):
                result.append(k)

        return result
        


