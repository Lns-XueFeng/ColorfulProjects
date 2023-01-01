import sys
from EnglishWords import EnglishWords


def main():
    display = "输入回车会得到一个随机的单词\n输入空格会得到按顺序得到十个单词" \
              "\n输入all会得到全部的单词\n输入其他任意输入将会退出程序\n"
    print(display)

    english_words = EnglishWords()
    get_ten = english_words.get_ten_word()  # 生成生成器
    while True:
        user_input = input("请输入：")

        if user_input == '':
            # 随机得到一个单词
            get_one = english_words.rand_get_one()
            print(get_one)

        elif user_input == ' ':
            # 每次都按顺序按步长为十来获得十个单词
            try:
                for i in next(get_ten):
                    print(i)
            except StopIteration:
                # for i in english_words.li_english_words:
                #     print(i)
                pass

        elif user_input == 'all':
            # 获得全部的单词
            all_the_words = english_words.get_all_words()
            print(all_the_words)

        else:
            sys.exit()


if __name__ == "__main__":
    main()
