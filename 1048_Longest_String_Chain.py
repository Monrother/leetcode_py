class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_depth = dict()
        len_word = dict()
        for word in words:
            word_len = len(word)
            if word_len in len_word:
                len_word[word_len].append(word)
            else:
                len_word[word_len] = [word]
            word_depth[word] = 1
        lens = list(len_word.keys())
        lens.sort(reverse=True)
        max_depth = 1
        for i in range(len(lens) - 1):
            if lens[i + 1] == lens[i] - 1:       # 建立连接
                for w1 in len_word[lens[i]]:
                    for w2 in len_word[lens[i + 1]]:
                        if self.isPredecessor(w1, w2):
                            word_depth[w2] = max(word_depth[w1] + 1, word_depth[w2])
                            max_depth = max(max_depth, word_depth[w2])
        return max_depth
    
    def isPredecessor(self, word1, word2):
        if len(word1) != len(word2) + 1:
            return False
        flag = False
        i = 0
        j = 0
        while i < len(word2):
            if word2[i] == word1[j]:
                i += 1
                j += 1
            else:
                if flag == False:
                    flag = True
                    j += 1
                else:
                    return False
        return True
        