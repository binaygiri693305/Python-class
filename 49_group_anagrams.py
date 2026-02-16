class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagrams = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return anagrams.values()