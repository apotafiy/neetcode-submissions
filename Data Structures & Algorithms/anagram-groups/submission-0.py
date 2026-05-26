class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = self.toChars(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return list(groups.values())
        

    
    def toChars(self, string):
        counts = [0 for _ in  range(26)]
        first_char = ord('a')
        for c in string:
            char_index = ord(c) - first_char
            counts[char_index] +=1
        return " ".join(str(n) for n in counts)