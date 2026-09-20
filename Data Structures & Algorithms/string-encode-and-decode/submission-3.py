class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the delimiter between the length and the string
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # The actual string begins after '#'
            start = j + 1
            end = start + length

            res.append(s[start:end])
            i = end

        return res



