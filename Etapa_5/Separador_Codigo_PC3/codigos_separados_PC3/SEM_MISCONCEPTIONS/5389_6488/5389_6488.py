from numpy import *

senha = input("Digite a senha criada: ")

ts = len(senha)
i = 0
total = 0

while (i < ts):
	if ((senha[i] == "A") or (senha[i] == "E") or (senha[i] == "I") or (senha[i] == "O") or (senha[i] == "U")):
		total = 3.15 + total
	else:
		total = 4.17 + total
	i = i + 1

print(round(total, 2))