class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for s in strs: # For every word in the list
            count = [0] * 26 # initiliaze array of 26 0s (for each a-z)
            
            for c in s: # For each letter in the current word
                # Getting unique int value for each letter in word ascii - ascii
                count[ord(c) - ord("a")] += 1 # Count +1 for every instance of a-z letter

            ans[tuple(count)].append(s)
        return ans.values()