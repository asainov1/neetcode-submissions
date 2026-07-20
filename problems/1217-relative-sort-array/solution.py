class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        for num in arr1:
            counter[num] += 1
        expected = []
        for num in arr2:
            while counter[num] > 0:
                expected.append(num)
                counter[num] -= 1

        for i in range(1001):
            while counter[i] > 0:
                expected.append(i)
                counter[i] -= 1

        return expected

