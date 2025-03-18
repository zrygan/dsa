class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        NICE = ""
        n = len(s)

        for start in range(n):
            seen = set()
            for end in range(start, n):
                seen.add(s[end])
                if self.is_nice(seen):
                    substring = s[start:end + 1]
                    if len(substring) > len(NICE):
                        NICE = substring
        
        return NICE

    def is_nice(self, seen: set) -> bool:
        for char in seen:
            if char.lower() not in seen or char.upper() not in seen:
                return False
        return True
