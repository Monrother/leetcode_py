class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = dict()
        for s in strs:
            tmp = "".join(sorted(s))        # sorted 可以对字符串处理，但返回的是 list 类型
            if tmp in str_dict:
                str_dict[tmp].append(s)
            else:
                str_dict[tmp] = [s]
        return list(str_dict.values())
        