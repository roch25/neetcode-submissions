class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = "".join(list(filter(lambda x: x.isalnum(), s)))
        return p[::-1].lower() == p.lower()
        