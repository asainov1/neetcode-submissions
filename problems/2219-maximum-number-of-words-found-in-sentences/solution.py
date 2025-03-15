class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        cnt_dict = {}
        for sentence in sentences:
            new_sentence = list(sentence.split(" "))
            cnt_dict[sentence] = len(new_sentence)
        sorted_dict = dict(sorted(cnt_dict.items(), key=lambda x: x[1]))
        return next(reversed(sorted_dict.values()))
            
