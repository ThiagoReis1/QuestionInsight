#UNIVERSIDADE FEDERAL DO AMAZONAS
#VANESSA FRANCLIN GARCIA
#MATÍCULA - 21602343	
#AVALIAÇÃO 06
#01/09/2016

from numpy import*

p = float(input(""))
x = array(eval (input("")))
y = array(eval(input("")))
t = (p)/(p + 1)
norma = 0
for i in range(size(x)):
	norma = ((abs(x[i] - 2*y [i])) ** t) + norma
norma = (norma ** (1/t))
print(round(norma,8))