from numpy import *

notas = array(eval(input("Informe os vetores da notas: ")))

reprovados = 0
vetor = zeros(size(notas), dtype=int)

for i in range(size(notas)):
	if notas[i] < 5:
		reprovados += 1
		
saida = zeros(reprovados, dtype=int)
insaida = 0
for i in range(size(notas)):
	if notas[i] < 5:
		saida[insaida] =  + i 
		insaida += 1
print(reprovados)	
print(saida)