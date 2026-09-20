class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def intergrise(num: str):
            def getdigit(s: str):
                digits = "0123456789"
                digit1 = 0
                while digits[digit1] != s:
                    digit1+=1
                return digit1

            res = 0   
            for i in range(len(num)-1, -1, -1):
                n = getdigit(num[len(num)-i-1])
                print(num[i],10 ** i)
                res += n * (10 ** i)

            return res 
        n1 = intergrise(num1)
        n2 = intergrise(num2)
        print(n1, n2)
        return str(n1*n2)
        
