# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Solution
For every figure from circle, triangle, rectangle and square exists python
script which defines functions: `area` and `perimeter`. Function `area` takes
figure parameters and returns area of described figure. Function `perimeter`
takes figure parameters and returns perimeter of described figure.

Parameters of figure can be either int or float. If any of figure parameter is
float the return value will be float due type conversions. Return value will
be float for circle in any case.

For every figure functions should be imported from file for that figure like
that:
```python
from figure import area, perimeter
```

## Figures

### Circle
Circle has only one parameter: radius. Radius parameter is called `r` in both
functions. Functions alwsay return float.

File for circle is [`circle.py`](../circle.py).

#### Code usage examples:
Get area of circle with radius of 1:
```python
area(1)
```
```python
area(r=1)
```

Get perimeter of circle with radius of 1:
```python
perimeter(1)
```
```python
perimeter(r=1)
```

Get perimeter of circle with radius of 2.3:
```python
perimeter(2.3)
```
```python
perimeter(r=2.3)
```

### Triangle
Circle has parameters: base, height and each side length.

Function `area` takes two parameters: `a` (length of triabgle base) and `h`
(length of triangle height). Each parameter can be either int or float.
Return value will be int or float if any of parameters is float.

Function `perimeter` takes three parameters: `a` (length of the first side),
`b` (length of the second side) and `c` (length of the third side). Order of
parameter is not necessary. Each parameter can be either int or float.
If any of parameter is float return value will be float, otherwise it will be
int.

File for tringle is [`triangle.py`](../triangle.py).

#### Code usage examples:
Get area of triangle with base length of 1 and height of 2:
```python
area(1, 2)
```
```python
area(a=1, h=2)
```
```python
area(h=2, a=1)
```

Get area of triangle with base length of 4.5 and height of 4:
```python
area(4.5, 4)
```
```python
area(a=4.5, h=4)
```
```python
area(h=4, a=4.5)
```

Get perimeter of triangle with sizes of 1, 2 and 3:
```python
perimeter(1, 2, 3)
```
```python
perimeter(1, 2, 3)
```
```python
perimeter(2, 1, 3)
```

Get perimeter of triangle with sizes of 4.1, 3.2 and 3.2:
```python
perimeter(4.1, 3.2, 2.3)
```
```python
perimeter(2.3, 4.1, 3.2)
```
```python
perimeter(3.2, 2.3, 4.1)
```


### Rectangle
Circle two parameters: sizes of two diffent sides.

Both functions takes paramters `a` and `b` which are sizes of two diffent
sides. Order of parameters is not necessary cause does not affect on results.
If any of parameter is float return value will be float, otherwise it will be
int.

File for rectangle is [`rectangle.py`](../rectangle.py).

#### Code usage examples:

Get area of rectangle with sizes 2 and 5:
```python
area(2, 5)
```
```python
area(a=2, b=5)
```
```python
area(b=5, a=2)
```

Get perimeter of rectangle with sizes 4.3 and 10.9:
```python
perimeter(4.3, 10.9)
```
```python
perimeter(a=4.3, b=10.9)
```
```python
perimeter(b=10.9, a=4.3)
```

Get perimeter of rectangle with sizes 2 and 5:
```python
perimeter(2, 5)
```
```python
perimeter(a=2, b=5)
```
```python
perimeter(b=5, a=2)
```

Get perimeter of rectangle with sizes 4.3 and 10.9:
```python
perimeter(4.3, 10.9)
```
```python
perimeter(a=4.3, b=10.9)
```
```python
perimeter(b=10.9, a=4.3)
```

### Square

Square has only one parameter: size.

Both functions takes paramters `a` which is size of square its side. If size
is float return value will be float, otherwise it will be int.

File for square is [`square.py`](../square.py).

#### Code usage examples:

Get area of square with radius of 1:
```python
area(1)
```
```python
area(r=1)
```

Get perimeter of square with radius of 1:
```python
perimeter(1)
```
```python
perimeter(r=1)
```

Get perimeter of square with radius of 2.3:
```python
perimeter(2.3)
```
```python
perimeter(r=2.3)
```

# Repository history:
- Added repository history comiits into docs [119003bcc6fe5a9e14079b5050c1d7d7a6fe3434](https://github.com/Lukramancer/geometric_lib/commit/119003bcc6fe5a9e14079b5050c1d7d7a6fe3434)
- Made detailed docs in docs/README.md [6b8b1b20ae534bc8fe9b75d7316adaa186ed1521](https://github.com/Lukramancer/geometric_lib/commit/6b8b1b20ae534bc8fe9b75d7316adaa186ed1521)
- Added formulas for triangle [4ade6d5c83219c724a47358ebc810def2ca1acf7](https://github.com/Lukramancer/geometric_lib/commit/4ade6d5c83219c724a47358ebc810def2ca1acf7)
- Made in file docs more precise [d41c75936afbd6911fd3c9e06689557f47a1e7a8](https://github.com/Lukramancer/geometric_lib/commit/d41c75936afbd6911fd3c9e06689557f47a1e7a8)
- Made docs in file circle.py [8f1d366db99ebc67212ebd4da6c9ca5caac55835](https://github.com/Lukramancer/geometric_lib/commit/8f1d366db99ebc67212ebd4da6c9ca5caac55835)
- Made docs in file trinagle.py [5fc54e72ca806790f374d34ad3c4322dd5d89a98](https://github.com/Lukramancer/geometric_lib/commit/5fc54e72ca806790f374d34ad3c4322dd5d89a98) 
- Made docs in file square.py [879cbfac0a8d2f1b468fb65e6baa3f231a2e2dea](https://github.com/Lukramancer/geometric_lib/commit/879cbfac0a8d2f1b468fb65e6baa3f231a2e2dea)
- Made docs in file rectangle.py [f89de74eebf9f6692df93708d466f35be5cea88d](https://github.com/Lukramancer/geometric_lib/commit/f89de74eebf9f6692df93708d466f35be5cea88d)
- Fixed error in rectanlge [26f8302544bde0424475feee11f63d3cf2a7e196](https://github.com/Lukramancer/geometric_lib/commit/26f8302544bde0424475feee11f63d3cf2a7e196)
- Added file rectangle.py [611e3cbc8dea921f3cc25771178f985bfff4e04d](https://github.com/Lukramancer/geometric_lib/commit/611e3cbc8dea921f3cc25771178f985bfff4e04d)
