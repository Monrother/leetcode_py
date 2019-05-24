class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1 = len(num1)
        n2 = len(num2)
        digits = [0] * (n1 + n2)
        for i in range(n1):
            for j in range(n2):
                dig1 = ord(num1[i]) - ord("0")
                dig2 = ord(num2[j]) - ord("0")
                digits[i + j + 1] += dig1 * dig2
        carry = 0
        for i in range(n1 + n2 - 1, -1, -1):
            temp = digits[i] + carry
            carry = temp // 10
            digits[i] = temp % 10
        print(digits)
        if digits[0] != 0:
            res = "".join([str(digits[i]) for i in range(n1 + n2)])
        else:
            res = "".join([str(digits[i]) for i in range(1, n1 + n2)])
        return res
