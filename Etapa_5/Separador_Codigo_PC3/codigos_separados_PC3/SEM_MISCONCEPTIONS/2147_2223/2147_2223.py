from numpy import *

holmes = input("Informe o cpf: ")
senha = ""
if len(holmes) == 11:
	for i in range(len(holmes)):
		if i % 2 != 0:
			senha = senha + holmes[i]
else:
	print("INVALIDO")
print(senha)