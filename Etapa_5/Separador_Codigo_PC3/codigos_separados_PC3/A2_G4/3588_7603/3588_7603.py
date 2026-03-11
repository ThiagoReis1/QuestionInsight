from numpy import *

vet = array(eval(input("aneis acertados: ")))

i = 0 #aneis acertados
acum = 10000 #pontuacao inicial

while i != size(vet):
	if vet[i] == 1:
		acum = acum * 2
	
	if vet[i] == 2:
		acum = acum
		
	if vet[i] == 3:
		acum = acum / 2
		
	if vet[i] == 4:
		acum = acum / 4
		
	i = i + 1

	
print(acum)
		


