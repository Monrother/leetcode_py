#coding: utf-8

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 判断两个字符串包含的字母相同
        if s1 == s2:
            return True

        d1 = {}
        d2 = {}
        for x in s1:
            if x in d1:
                d1[x] += 1
            else:
                d1[x] = 1
        for x in s2:
            if x in d2:
                d2[x] += 1
            else:
                d2[x] = 1
        if d1 != d2:
            return False
        t1 = {}
        t2 = {}
        for l in range(1, len(s1)):
            cur = s1[l - 1]
            if cur in t1:
                t1[cur] += 1
                if t1[cur] == 0:
                    t1.pop(cur)
            else:
                t1[cur] = 1

            cur = s2[l - 1]
            if cur in t1:
                t1[cur] -= 1
                if t1[cur] == 0:
                    t1.pop(cur)
            else:
                t1[cur] = -1
            if len(t1.keys()) == 0:
                if self.isScramble(s1[:l], s2[:l]) and self.isScramble(s1[l:], s2[l:]):
                    return True

            cur = s1[l - 1]
            if cur in t2:
                t2[cur] += 1
                if t2[cur] == 0:
                    t2.pop(cur)
            else:
                t2[cur] = 1

            cur = s2[len(s1) - l]
            if cur in t2:
                t2[cur] -= 1
                if t2[cur] == 0:
                    t2.pop(cur)
            else:
                t2[cur] = -1
            if len(t2.keys()) == 0:
                if self.isScramble(s1[:l], s2[-l:]) and self.isScramble(s1[l:], s2[:-l]):
                    return True
        return False


                 


if __name__ == "__main__":
    str1 = "abcdee"
    str2 = 
    d1 = {}
    for x in str1:
        if x in d1:
            d1[x] += 1
        else:
            d1[x] = 1