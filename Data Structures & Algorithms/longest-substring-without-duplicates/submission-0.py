class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setC = set() # key: value, char: ord(char)
        l, r = 0, 1
        maxS = 1

        if not s:
            return 0

        for r in range(len(s)):
            while s[r] in setC:
                setC.remove(s[l])
                l += 1
            setC.add(s[r])
            maxS = max(maxS, len(setC))
            
        return maxS