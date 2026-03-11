from numpy import*
n = array(eval(input('vetor de danos:')))
i = 0
a = 1
cont = 0
while(size(n) > i):			
	cont = cont + n[i] * a
	i = i + 1
	a = a + 1 
	
print(cont)