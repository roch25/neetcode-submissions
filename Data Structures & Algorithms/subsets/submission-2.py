class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)

        for k in range(n // 2 + 1):

            if k == 0:
                result.append([])
            else:
                i = list(range(k))

                while True:
                    result.append([nums[x] for x in i])

                    j = k - 1

                    while j >= 0 and i[j] == n - k + j:
                        j -= 1

                    if j < 0:
                        break

                    i[j] += 1

                    for x in range(j + 1, k):
                        i[x] = i[x - 1] + 1

            
            other = n - k

            if other != k:
                i = list(range(other))

                while True:
                    result.append([nums[x] for x in i])

                    j = other - 1

                    while j >= 0 and i[j] == n - other + j:
                        j -= 1

                    if j < 0:
                        break

                    i[j] += 1

                    for x in range(j + 1, other):
                        i[x] = i[x - 1] + 1

        return result