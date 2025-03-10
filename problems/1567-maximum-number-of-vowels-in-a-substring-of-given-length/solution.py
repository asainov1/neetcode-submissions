class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # vowels = ['a','e','i','o','u']
        # vowels_pos = [idx for idx, letter in enumerate(s) if letter in vowels]
        # j, l = len(vowels_pos) - 1, 0
        # cnt_dict = defaultdict(int)
        # cnt = 0
        # while l < j:
        #     if s[l] in cnt_dict and cnt <= k:
        #         cnt_dict[s[l]] += 1            
        #     else:
        #         cnt_dict[s[l]] = 1
        #         cnt += 1
        #     l += 1
        # return len(cnt_dict.keys())
        l, cnt, res = 0, 0, 0
        vowelSet = {'a','e','i','o','u'}
        for r in range(len(s)):

            cnt += 1 if s[r] in vowelSet else 0
            if r - l + 1 > k:

                cnt -= 1 if s[l] in vowelSet else 0
                l += 1
            res = max(res, cnt)
        return res
        
