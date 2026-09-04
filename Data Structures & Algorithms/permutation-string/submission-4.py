class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        finder = s1[0]

        indices = [i for i in range(len(s2)) if s2.startswith(finder, i)]
        for i in indices:
            for j in range(len(s1), 0, -1):
                print("".join(sorted(s2[i-j+1:i-j+1+len(s1)])))
                # print(s2[i-j+1:i-j+1+len(s1)], i)
                # print("".join(sorted(s2[i-j+1:i-j+1+len(s1)])),"".join(sorted(s1)))
                if "".join(sorted(s2[i-j+1:i-j+1+len(s1)])) == "".join(sorted(s1)):
                    return True


        return False