from numpy import *

x = input("Senha: ").upper()

i = 0
tp = 0

custo_senha1 = 1.12
custo_senha2 = 1.18

x_list = list(x)
v_list = ["A", "E", "I", "O", "U"]

while i < size(x_list):
	if x_list[i] not in v_list:
		tp += custo_senha2
	else:
		tp += custo_senha1
	i += 1

print(round(tp, 2))
		