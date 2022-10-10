def task1():
    The_First_Number = input("Введите первое число a: ")
    The_Second_Number = input("Введите второе число b: ")
    The_Third_Number = input("Введите третье число: ")

    if The_First_Number > The_Second_Number:
        print(The_Second_Number)

    elif The_Second_Number > The_First_Number:
        print(The_First_Number)

    elif The_Third_Number > The_First_Number:
        print(The_First_Number)
    elif The_Third_Number > The_Second_Number:
        print(The_Second_Number)

    elif The_First_Number > The_Third_Number:
        print(The_Third_Number)

    else:
        print(The_Third_Number)

def task2():
    print("Введите коэффициенты уравнения типа: ax^2+bx+c")


    a_var = int(input("a: "))
    b_var = int(input("b: "))
    c_var = int(input("c: "))


    D = (b_var* b_var) - 4 * a_var * c_var

    if D > 0:
        print("ДА")

    elif D == 0:
        print("ДА")

    else:
        print("Нет")

def task3():
    City_Caption = input()
    City_List =  City_Caption.split(' ')

    if 'Moscow' not in City_List: 
        City_List.append('Moscow')
    print(City_List)
    


def task4():
    a_sec = input("Введите время в секундах: ")

    b_sec = input("Введите время в минутах: ")

    if a_sec > b_sec:
        print(a_sec)

    else:
        print(b_sec) 

        

def task5():
    while True:
        print("1. Кафедра ТК:")
        print("2. Факультет ФИСТ")
        print("3. Каферда Радиотехника")
        print("0. Выйти")
        User_Inpt = input("Выберите пункт: ")

        if User_Inpt == "1":
            print("Выбран 1 пункт")
        elif User_Inpt == "2":
            print("Выбран 3 пункт")
        elif User_Inpt == "3":
            print("Выбран 3 пункт")
        elif User_Inpt == "0":
            break
        else:
            print("Вы ввели не правильное значение")




