class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        # Считаем буквы в s1 и первом окне s2
        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord("a")
            window_index = ord(s2[i]) - ord("a")
            s1_count[s1_index] += 1
            window_count[window_index] += 1

        if s1_count == window_count:
            return True

        # Двигаем окно
        for right in range(len(s1), len(s2)): #3, 4 ,5 ,6
            incoming = ord(s2[right]) - ord("a")
            window_count[incoming] += 1
            left = right - len(s1)
            outgoing = ord(s2[left]) - ord("a")
            window_count[outgoing] -= 1
            
            current_window = s2[left + 1:right + 1]

            if s1_count == window_count:
                return True

        return False
