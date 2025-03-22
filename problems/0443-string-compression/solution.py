class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        cnt, i = 0, 0
        while i < len(chars):
            letter = chars[i] # pointer for letters
            cnt = 0  # pointer for cnt consequitive
            while i < len(chars) and chars[i] == letter:
                cnt += 1 # increment 
                i += 1 # just left pointer
            chars[ans] = letter
            ans += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[ans] = c
                    ans += 1
        return ans


