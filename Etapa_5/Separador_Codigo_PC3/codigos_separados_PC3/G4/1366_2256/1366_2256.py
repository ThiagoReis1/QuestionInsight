from math import*
a = radians(float(input("qual o a da flecha?")))
vo = (float(input("qual a vo inicial?")))
g = 9.8
d = (vo**2) *sin(2*a)/g
print(round(d,2))

