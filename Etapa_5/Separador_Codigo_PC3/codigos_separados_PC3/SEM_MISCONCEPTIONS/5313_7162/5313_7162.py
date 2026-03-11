valor = float(input("Valor em BogoMips:"))

ano = 2018
processador_1 = 7206.14
processador = processador_1 + 0.65*processador_1

while processador <= valor:
	ano = ano+1
	processador = processador + 0.65*processador
print(ano+1)	