from numpy import*

turmas = array(eval(input("Digite as turmas de possibilidade de tocar")))
acumu= 0

for i  in range(size(turmas)):
	if turmas[i]%5==0:
	   acumu+=1
	
print(acumu)

z= zeros(acumu, dtype=int)
j=0

for i in range(size(turmas)):
	if turmas[i]%5==0:
		z[j]=i
		j+=1
		
		
print(z)