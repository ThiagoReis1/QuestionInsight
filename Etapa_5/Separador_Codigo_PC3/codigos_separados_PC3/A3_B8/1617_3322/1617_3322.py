from numpy import *
espada = input().upper()
nivel = array(eval(input()))
i = 0
soma = 0
while i <= size(espada):
	if espada[i] == "CENOURA":
		dano_e = 2
	elif espada[i] == "FERRO":
		dano_e = 4
	elif espada[i] == "DWARVEN":
		dano_e = 8
	elif espada[i] == "ELVEN":
		dano_e = 11
	elif espada[i] == "DAEDRIC":
		dano_e = 14
	soma = soma + dano_e
	i = i + 1
print(soma)
	