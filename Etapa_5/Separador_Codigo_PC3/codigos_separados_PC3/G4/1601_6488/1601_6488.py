from numpy import *

t = array(eval(input("Digite o tempo de chegada dos corredores em segundos: ")))

st = size(t)
i = 0

while (i < st):
	if (t[i] == min(t)):
		print(i)
	i = i + 1