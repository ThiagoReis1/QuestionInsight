from numpy import *
t = array(eval(input("Duracao dos banhos: ")))
p = array(eval(input("Percentual de abertura durante os banhos: ")))
n = size(t)
consumo = 0
for i in range(n):
	consumo = consumo + 5*(t[i]*p[i])/100
consumo = round(consumo, 2)
print(consumo)