from numpy import*
v= array(eval(input("monte o vetor de 75 passageiros")))
i= 0
dif= v[-1]
passageiro= 0
while(i<size(v)):
	passageiro= passageiro + sum(v) 
	i= i+1
print(passageiro)
	
	