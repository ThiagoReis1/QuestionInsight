from math import *
c_l= float(input("qual o comprimento do lado do octogono: "))
v_a= c_l / (2 * tan (pi / 8))
a = 4 * c_l * v_a

print(round(a, 2))
