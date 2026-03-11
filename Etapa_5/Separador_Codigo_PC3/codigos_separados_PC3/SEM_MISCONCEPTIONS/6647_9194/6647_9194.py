from numpy import*
notas= array(eval(input('inserir vetor de notas:')))

p= [2,1,5]
i=0

#mp = n*p+.../p+p...
while i<size(notas):
	if size(notas)==size(p):
		i= (notas[0]*p[0]+notas[1]*p[1]+notas[2]*p[2])/(p[0]+p[1]+p[2])
		
print(round(i,2))
		
