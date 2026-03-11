from numpy import *
entra = array(eval(input("qtde de pessoas q entraram: ")))
sai = array(eval(input("qtde de pessoas q sairam: ")))
onibus = 0
i = 0
total_passageiros = 75
while (total_passageiros >= onibus):
	onibus = onibus - sai[i] + entra[i]
	i = i + 1
print(onibus)