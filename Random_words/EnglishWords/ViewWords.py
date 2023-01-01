import random


class EnglishWords:
    def __init__(self):
        """初始化英语单词列表"""
        self.li_english_words = []
        self.deal_li_english_words()   # 将单词添加至li_english_words
        self.numbers_of_li = len(self.li_english_words)
        self.left_of_words = None   # 接受最后剩余的单词

    def deal_li_english_words(self):
        with open("./EnglishWords.txt", 'r', encoding="utf-8") as fp:
            # line_of_txt = fp.readlines()   # 不建议迭代，直接迭代文件对象较快
            for line in fp:
                if len(line) != 2:
                    self.li_english_words.append(line)

        while True:
            if '\n' in self.li_english_words:
                self.li_english_words.remove('\n')
                continue
            break

    def rand_get_one(self):
        return random.choice(self.li_english_words)

    def get_ten_word(self):
        index = 0
        while True:
            yield self.li_english_words[index: index+10]
            index = index + 10
            if (index + 10) >= self.numbers_of_li:
                difference = len(self.li_english_words) - index   # 得到剩余不足10个的差值
                left_of_words = self.li_english_words[index: index + difference]   # 得到单词列表中剩下的单词
                self.left_of_words = left_of_words
                return

    def get_all_words(self):
        all_words = ""
        for words in self.li_english_words:
            all_words = all_words + words
        return all_words
