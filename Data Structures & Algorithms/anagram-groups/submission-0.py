class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        if len(strs) == 1:
            return [strs]
        for st in strs:
            key = "".join(sorted(st)) 
            if key in seen:
                seen[key].append(st)
            else:
                seen[key] = [st]
        return list(seen.values())