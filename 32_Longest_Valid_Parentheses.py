class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        max_len = 0
        cur_len = 0
        last = 0
        for x in s:
            if x == '(':
                l += 1
            elif x == ')':
                if l == 0:
                    last = 0
                else:
                    cur_len += 2
                    l -= 1
                    if l == 0:
                        last += cur_len
                        cur_len = 0
                        max_len = max(last, max_len)
        # max_len1 = max(max_len1, cur_len)

        last = 0
        cur_len = 0
        l = 0
        # max_len2 = 0 
        for x in s[::-1]:
            if x == ')':
                l += 1
            elif x == '(':
                if l == 0:
                    last = 0
                else:
                    l -= 1
                    cur_len += 2
                    if l == 0:
                        last += cur_len
                        cur_len = 0
                        max_len = max(last, max_len)
        # max_len = max(max_len, cur_len)
        return max_len

# )))
# ()(())
# )
# ()
# )
# (())()()
# )
# ( () ((())) ) () 
# )))))
# (())
# ))
# (()())
# )
# (())()
# )
# ()
# )))
# (())
# )
# ()
# ))
# ((((()()))))
# )
# ()()
# ))
# ( ()((())((())())()()()()((()((((())))(()))(()()()))))
# (
# () 
# ((   
# ((()))(((((()))())())) 
# (((