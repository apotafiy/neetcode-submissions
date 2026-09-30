class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        chars = {}
        # chars = {s[0]: 1}
        max_ = 0

        def getMax(char_count: dict) -> int:
            m = 0
            for v in char_count.values():
                m = max(m, v)
            return m
        
        while l < len(s):
            while r < len(s):
                chars[s[r]] = chars.get(s[r], 0) + 1
                most_common = getMax(chars)
                r += 1
                if ((r - l) - most_common) > k:
                    break
                max_ = max(max_, r - l)
                # print(f"l: {l}")
                # print(f"r: {r}")
                # print(f"max_: {max_}")
                # print(f"most_common: {most_common}")
                # print(f"remaining: {(r - l + 1) - most_common}")
                # print(chars)
                # print("- - - - - - - - - - - - - - ")
            if l < len(s):
                chars[s[l]] = chars[s[l]] - 1
            l += 1
        return max_

