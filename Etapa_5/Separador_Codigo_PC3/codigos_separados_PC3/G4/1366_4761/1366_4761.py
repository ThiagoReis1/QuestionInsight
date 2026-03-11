from math import*
a = radians(float(input('angulo:')))
v = float(input('velocidade inicial:'))
g = 9.8
d = v**2*(sin(2*a)/g)
print(round(d, 2))
