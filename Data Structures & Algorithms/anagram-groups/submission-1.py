class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            rep = ''.join(sorted(word))
            if rep in output:
                output[rep].append(word)
            else:
                output[rep] = [word]
            
        return list(output.values())