r = open("text.txt", 'r')
word1=input('input word1:')
word2=input('input word2:')
pytxt=''
words_all = r.readlines()
for words in words_all:
    w=words.split()
    for pywords in w:
        if pywords == word1:
            pywords = word2
        pytxt += f'{pywords} '
    pytxt = f'{pytxt}\n'
new_txt = open('newtext.txt', 'w')
new_w = new_txt.write(pytxt)

