class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        end = 0
        max_ = 0
        chars = set()
        # xyzz
        # xyaazz
        while start < len(s) and end < len(s):
            end_val = s[end]
            if end_val in chars:
                while start < end:
                    chars.remove(s[start])
                    start += 1
                    if s[start - 1] == end_val:
                        break
            else:
                chars.add(end_val)
                end += 1
                max_ = max(max_, len(chars))
        return max_
            


        