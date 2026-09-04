class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        length = 0
        seq = ""
        while i < len(s):
            if s[i] not in seq:
                seq += s[i]
            else:
                index = seq.find(s[i])
                seq = seq[index+1:] + s[i]
            length = length if len(seq) < length else len(seq)
            i+=1
            
        if i == len(s):
            length = length if len(seq) < length else len(seq)
        
        return length
        