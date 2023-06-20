def conclusion():
    print('Будут работать:')
    while True:
        answer_2 = 2 #int(input('Вывести списком (1) или по пультам (2) ? '))
        if answer_2 == 1:
            print(', '.join(team))
            break
        elif answer_2 == 2:
            for i in range(len(team)):
                print(team[i], end= ' ')
                if i % 2 == 1:
                    print()
                if i == len(team) - 1 and i % 2 == 0:
                    print()
            break
        else:
            print('Ошибка ввода')
