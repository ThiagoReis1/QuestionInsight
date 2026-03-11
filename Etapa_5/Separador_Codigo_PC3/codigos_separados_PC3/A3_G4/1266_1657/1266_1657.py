#Universidade Federal do Amazonas
#25/08/2016
# Matricula 21553775
from numpy import*
from math import*
p = float(input("Digite "))
x = array(eval(input("Digite ")))
y = array(eval(input("Digite")))
h = 0
n= 0
j = 0
t = (p)/ (p -1)
xy = (2*x - y)
for i in xy:
	n = n + (abs(i) ** t)
v = n ** (1/t)
print(round(v, 4))