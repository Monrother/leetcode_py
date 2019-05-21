## 38. Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        seq = "1"
        if n == 1:
            return seq
        for i in range(n - 1):
            tmp = ""
            last = " "
            cnt = 0
            for c in seq:
                if c != last:
                    if cnt != 0:
                        tmp += str(cnt) + last
                    last = c
                    cnt = 1
                else:
                    cnt += 1
            tmp += str(cnt) + last
            seq = tmp
        return seq
