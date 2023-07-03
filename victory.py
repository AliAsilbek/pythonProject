# Pushkin - 1799 Tolstoy - 1828 Dostoevsky - 1821  Ray Bradbury - 1920 Mayakovsky - 1893
pu = ''
to = ''
do = ''
re = ''
ma = ''
score = 5
while True:
    a = input('Start the game? (Yes/no) ')
    if a == "no":
        break
    elif a == "yes":
        pu = input('what year was A.S. Pushkin born? ')
        to = input('what year was Lev Nikolayevich Tolstoy born? ')
        do = input('what year was Fyodor Mikhailovich Dostoevsky born? ')
        re = input('what year was Ray Douglas Bradbury born? ')
        ma = input('what year was Vladimir Vladimirovich Mayakovsky born? ')
        if not pu == "1799":
            score = score - 1
        if not to == "1828":
            score = score - 1
        if not do == "1821":
            score = score - 1
        if not re == "1920":
            score = score - 1
        if not ma == "1893":
            score = score - 1
        print('congratulations! You gained', score, "out of 5")
        print('You lost', score, "out of 5")
        print('your percentage of correct answers:', score * 100 / 5)
        print('your percentage of uncorrect answers:', (5 - score) * 100 / 5)
