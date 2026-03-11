#let's start!
from math import *
#okay, first i will define 'a' as venom quantity

a = float(input("qual a quantidade de veneno injetada, em gramas?"))

#and then, i will apply 'a' to formulas

c_colmeia = (a/5) * sqrt(9/5)
g_alho = a**2/pi
o_troll = sqrt(5*a/3)

#and then print the results

print(round(c_colmeia, 2))
print(round(g_alho, 2))
print(round(o_troll, 2))