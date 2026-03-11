from numpy import*

nota = array(eval(input("nota: ")))


contap= 0
for i in range(0 , size(nota)):
	if(nota[i] >= 5):
		contap += 1
		
saida = zeros(contap, dtype = int)
cont = 0
for i in range(size(nota)):
	if(nota[i] >= 5):
		saida[cont] = i
		cont += 1
		
print(contap)	
print(saida)
		
		
	
	
	
	