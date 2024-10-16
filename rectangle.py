def area(a, b): 
    '''
    Возвращает площадь прямоугольника
        
        Параметры:
            a (int | float): длина первой стороны прямоугольника
            b (int | float): длина второй стороны прямоугольника

        Возвращаемое значение:
            area (int | float): площадь прямоугольника со сторонами
                длин a и b; может быть как целым числом (int), так и
                с плавающей точкой (float), в зависимости от типов
                входных данных
        
        Примеры вызова:
            area(1, 2)
            area(2, 1)
            area(1.0, 1)
            area(b=1, a=1.0)
        Получаемые значения:
            2
            2
            1.0
            1.0
    '''
    return a * b 

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника
        
        Параметры:
            a (int | float): длина первой стороны прямоугольника
            b (int | float): длина второй стороны прямоугольника

        Возвращаемое значение:
            perimeter (int | float): периметр прямоугольника со
                сторонамм длин a и b; может быть как целым
                числом (int), так и с плавающей точкой (float),
                в зависимости от типов входных данных
        Примеры вызова:
            perimeter(1, 2)
            perimeter(2, 1)
            perimeter(1.0, 1)
            perimeter(b=1, a=1.0)
        Получаемые значения:
            6
            6
            4.0
            4.0
    '''
    return 2 * (a + b)

