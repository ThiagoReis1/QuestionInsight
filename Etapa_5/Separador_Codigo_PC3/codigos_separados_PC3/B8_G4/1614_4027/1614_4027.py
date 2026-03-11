from numpy import *
nome = array(eval(input("Nomes dos alimentos: ")))
q = array(eval(input("Quantidade em gramas dos alimentos: ")))
n = size(q)
i = 0
cal = 0
while(i < n):
	if(nome[i] == "BANANA"):
		cal = cal + int(q[i])*0.97
	elif(nome[i] == "BIFE"):
		cal = cal + int(q[i])*2.95
	elif(nome[i] == "FEIJOADA"):
		cal = cal + int(q[i])*1.27
	elif(nome[i] == "OMELETE"):
		cal = cal + int(q[i])*1.04
	elif(nome[i] == "TOMATE"):
		cal = cal + int(q[i])*0.2
	i = i + 1
print(round(cal,2))