number = 23
running = True

while running:
    guess = int(input('Введите целое число: '))

    if guess == number:
        print('Поздравляю, вы угадали,') # Начало нового блока
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого.') # Ещё один блок
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
print('Завершение.')