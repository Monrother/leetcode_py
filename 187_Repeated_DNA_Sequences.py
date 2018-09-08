class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        if len(s) <= 10:
            return ret
        seqset = set()
        char_map = {'A': 0, 'G':1, 'T':2, 'C':3}
        num = 0
        for c in s[:10]:
            num <<= 2
            num += char_map[c]
        seqset.add(num)
        seqset2 = set()
        for i in range(10, len(s)):
            c = s[i]
            num &= 0x3ffff
            num <<= 2
            num += char_map[c]
            if num in seqset and num not in seqset2:
                ret.append(s[i-9: i+1])
                seqset2.add(num)
            elif num not in seqset2:
                seqset.add(num)
        return ret