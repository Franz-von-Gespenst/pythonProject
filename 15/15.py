import random


def func():
    print("Хотите начать сначала? (1 - ДА )")
    s = int(input())
    if s != 1:
        return False
    return True


print("{Приветственное сообщение от игры}")
k = True
while k:
    num = random.randint(0, 100)
    lose = True
    for i in range(0, 5):
        a = int(input("число = "))
        if a > num:
            if i != 4:
                print("Загаданное число меньше")
        elif a < num:
            if i != 4:
                print("Загаданное число больше")
        elif a == num:
            print("Поздравляю! Вы угадали")
            k = func()
            lose = False
            break
    if lose:
        print("Вы проиграли. Было загадано: ", num)
        k = func()
