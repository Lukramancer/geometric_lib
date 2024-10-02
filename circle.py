import math


def area(r):
    '''
    Возвращает площадь круга
        
        Параметры:
            r (int | float): длина радиуса круга

        Возвращаемое значение:
            area (float): площадь круга
    '''

    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга
        
        Параметры:
            r (int | float): длина радиуса круга

        Возвращаемое значение:
            area (float): периметр круга
    '''

    return 2 * math.pi * r

