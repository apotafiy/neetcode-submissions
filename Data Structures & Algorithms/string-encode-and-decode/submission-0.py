class Solution:
    delimeter = '#'

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append(self.delimeter)
            encoded.append(s)
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = []
        left = 0
        right = 0
        while right < len(s):
            while right < len(s):
                right += 1
                if s[right] == self.delimeter:
                    break
            if right >= len(s):
                break
            length = int(s[left: right])
            right += 1
            decoded.append(s[right: right + length])
            right = right + length
            left = right
        return decoded