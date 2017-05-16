"""
61. number of lines, words, characters
"""
chars=0
words=0
lines=0
f=open('source_59.txt','r')
for i in f:
    lines=lines+1
    words=len(i.split())+words
    chars=len(i)+chars
print "Number of Lines,Words,Chars in the given file respectively are",lines,words,chars
