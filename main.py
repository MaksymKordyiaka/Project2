'''
Дано список елементів. Створити програму, яка при взаємодії з користувачем буде виводити меню згідно якого- користувач
може обирати варіанти взаємодії зі списком.

Після чого користувач обирає варіант- що він хоче зробити (для прикладу insert), далі програма має запитувати який тип
елементу ми хочемо додати (стрічка / цифра) і в залежності від вибору- чекатиме від користувача на введення відповідний
тип даних + індекс, на який необхідно додати цей елемент.

Якщо такий елемент вже є- програма виведе повідомлення, що елемент вже існує, чи бажаєте додати ще один? Якщо так- значить
додаємо, якщо ні- завершуємо роботу.

В кінці виконання- програма виводить на екран список. При роботі для користувача доступні такі методи:
 «append(), insert(), remove(), index()»
'''

lst = [1, 2, 3, 4, 5,'a','b','c','d','e']
option = input('Оберіть варіант взаємодії: ')
option == 'append' or 'insert' or 'remove' or 'index'
if option == 'append':
    type = input('Виберіть тип: ')
    if type == 'int':
        element = int(input('Введіть елемент: '))
        if element in lst:
            print('Такий елемент вже існує, чи бажаєте додати ще один?')
            answer = input()
            if answer == 'так':
                element1 = int(input('Введіть ще раз елемент: '))
                lst.append(element1)
                print(lst)
        else:
             lst.append(element)
             print(lst)
    elif type == 'str':
        element = input('Введіть елемент: ')
        if element in lst:
            print('Такий елемент вже існує, чи бажаєте додати ще один?')
            answer = input()
            if answer == 'так':
                element1 = input('Введіть ще раз елемент: ')
                lst.append(element1)
                print(lst)
        else:
            lst.append(element)
            print(lst)

elif option == 'insert':
    type = input('Виберіть тип: ')
    if type == 'int':
        element = int(input('Введіть елемент: '))
        if element in lst:
            print('Такий елемент вже існує, чи бажаєте додати ще один?')
            answer = input()
            if answer == 'так':
                element1 = int(input('Введіть ще раз елемент: '))
                index = int(input('Введіть індекс: '))
                lst.insert(index, element1)
                print(lst)
        else:
            index = int(input('Введіть індекс: '))
            lst.insert(index, element)
            print(lst)
    elif type == 'str':
        element = input('Введіть елемент: ')
        if element in lst:
            print('Такий елемент вже існує, чи бажаєте додати ще один?')
            answer = input()
            if answer == 'так':
                element1 = input('Введіть ще раз елемент: ')
                index = int(input('Введіть індекс: '))
                lst.insert(index, element1)
                print(lst)
        else:
            index = int(input('Введіть індекс: '))
            lst.insert(index, element)
            print(lst)

elif option == 'remove':
    type = input('Виберіть тип: ')
    if type == 'int':
        element = int(input('Введіть елемент, який хочете видалити: '))
        lst.remove(element)
        print(lst)
    elif type == 'str':
        element = input('Введіть елемент, який хочете видалити: ')
        lst.remove(element)
        print(lst)

elif option == 'index':
    type = input('Виберіть тип: ')
    if type == 'int':
        element = int(input('Введіть елемент: '))
        print(lst.index(element))
    elif type == 'str':
        element = input('Введіть елемент: ')
        print(lst.index(element))