from random import randint


def number_game():
    number = randint(1, 100)

    print('1から100までのどれかを思い浮かべています。')
    guess = int(input('いくつだと思いますか？'))

    while guess:
        if number == guess:
            print('正解です！答えは', number, 'でした')
            break
        elif number > guess:
            print('違います。もっと大きいです。')
        else:
            print('違います。もっと小さいです。')
        guess = int(input('いくつだと思いますか？'))


def greet():
    name = input('名前を教えて？')
    print('こんにちは、', name, 'さん')


number_game()
