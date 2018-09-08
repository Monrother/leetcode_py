class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l2 == 0:
            return 0

        next = [-1]

        for i in range(1, l2):
            if needle[i] == needle[next[-1] + 1]:
                next.append(next[-1] + 1)
            else:
                next.append(-1)
        print "next: "
        print next
        start = 0
        cur = 0
        while start <= l1 - l2:
            if haystack[start + cur] == needle[cur]:
                cur += 1
                if cur == l2:
                    return start
            else:
                if next[cur - 1] == -1:
                    start += cur
                    cur = 0
                else:
                    start += next[cur - 1]
                    cur -= next[cur - 1]

if __name__ == "__main__":
    s = Solution()
    print(s.strStr("abababaca", "ababaca"))
