import employees as em
import completed_work as cw


def option():
    print("\nВас приветствует помошник Григорий!")
    chek = int(input('Введите что хотите сделать: \n \
    1: Поиск ID сотрудника по фамилии \n \
    2: Посмотреть выполненные работы и должность \n \
    3: Выход\n \
    Ваш выбор: '))

    while True:
        try:
            if chek == 1:
                Surn = str(input("Введите фамилию сотрудника: "))
                if Surn in em.employees_card['Фамилия']:
                    index = em.employees_card['Фамилия'].index(Surn)
                    print(f"{em.employees_card['ID'][index]}, {em.employees_card['Имя'][index]},{em.employees_card['Фамилия'][index]}\n,{em.employees_card['Дата рождения'][index]}, {em.employees_card['Должность'][index]}")
                    print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
                    num = input()
                    if num == 'Y' or 'y' or 'У' or 'у':
                        option()
                    exit()

            elif chek == 2:
                c = input('Введите ID сотрудника для просмотра работ: ')
                if c in cw.completed_work['ID']:
                    index = cw.completed_work['ID'].index(c)
                    print(f" Выполняет работы - {cw.completed_work['Тип работы'][index]}\n\, стоимость работ - {cw.completed_work['Стоимость работ'][index]}, Имя: {em.employees_card['Имя'][index]}, Фамилия - {em.employees_card['Фамилия'][index]}, и Должность: {em.employees_card['Должность'][index]}")
                    print('\nХотите выполнить другую операцию??? Y или N: ')
                    num = input()
                    if num == 'Y' or 'y' or 'У' or 'у' or 'н':
                        option()
                    exit()
            elif chek == 3:   
                    print('goodbay my love')
                    exit()

            else:
                print("Ошибка - это не число")
                option()

        except ValueError:
            print("Ошибка - это не число")
        
        
        
        
        
        
        
        
        
        #try:
        #    # Если ввели не число, выполнение прервется здесь ...
        #    chek = int(raw_input)
        #    print("Введите 1, 2, или 3")
        #    option()
        #except ValueError:  # (реакцию настроили только на ошибки определенного типа)
        # ... и тогда прыгнет сюда
        #    print("Введите 1, 2, или 3")
        #    option()


option()
