# Задание 3. Числовые типы, операции и преобразования
import math

print("Эксперимент A. int и арифметические операторы")
x = 17
y = 5

print("x + y =", x + y, type(x + y))
print("x - y =", x - y, type(x - y))
print("x * y =", x * y, type(x * y))
print("x / y =", x / y, type(x / y))
print("x // y =", x // y, type(x // y))
print("x % y =", x % y, type(x % y))
print("x ** y =", x ** y, type(x ** y))
print()

print("Эксперимент B. Большие целые числа")
print(2 ** 1000)
print(type(2 ** 1000))
print()

print("Эксперимент C. float")
result = 0.1 + 0.2
print("result =", result)
print("result == 0.3:", result == 0.3)
print("result - 0.3 =", result - 0.3)
print("math.isclose(result, 0.3):", math.isclose(result, 0.3))
print()

print("Эксперимент D. bool, complex и преобразования")
print(int("42"), type(int("42")))
print(float("3.14"), type(float("3.14")))
print(str(2026), type(str(2026)))
print(bool(0), type(bool(0)))
print(bool(-1), type(bool(-1)))
print(bool(""), type(bool("")))
print(bool("False"), type(bool("False")))
z = complex(2, -3)
print(z, type(z))
print("real =", z.real, "imag =", z.imag)

