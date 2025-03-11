class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram = ''.join(sorted(p))
        win = ''
        inds = []
        win_start = 0
        for char in s:
            win += char
            if len(win) == len(anagram):
                if ''.join(sorted(win)) == anagram:
                    inds.append(win_start)
                win = win[1:]
                win_start += 1
        return inds


