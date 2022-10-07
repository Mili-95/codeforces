def word_translate(word, wordr):
    if word[::-1] != wordr:
        return 'NO'
    else:
        return 'YES'


x = input()
y = input()
print(word_translate(x,y))