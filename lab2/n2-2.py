import re


class Statistics:
    """Class Statistics"""

    def __init__(self, info):
        self.info = info

    def f_symb(self):
        counter = 0
        try:
            file1 = open(self.info, 'r')
            for line in file1:
                counter += len(line)
            file1.close()
            return f'smb: {counter}\n'
        except IOError:
            raise IOError("Error 1")

    def f_words(self):
        try:
            file1 = open(self.info, 'r')
            text = file1.read()
            text = text.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ').replace('\n', ' ')
            w_numb = len(text.split())
            file1.close()
            return f'wrd: {w_numb}\n'
        except IOError:
            raise IOError("Error 2")

    def f_sent(self):
        try:
            file1 = open(self.info, 'r')
            text = file1.read()
            s_numb = len(re.split('! |\? |\. |\...', text))
            file1.close()
            return f'snt: {s_numb}'
        except IOError:
            raise IOError("Error 3")


x = Statistics("text.txt")
print(x.f_symb() + x.f_words() + x.f_sent())
