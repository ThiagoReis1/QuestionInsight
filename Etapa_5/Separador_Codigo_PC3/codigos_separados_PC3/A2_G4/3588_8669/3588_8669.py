from numpy import*
n= array(eval(input("n: ")))
i= 0
ponto= 10000
while i< size(n) :
	if n[i] == 1:
		ponto= ponto*2
	if n[i] == 2:
		ponto = ponto
	if n[i] == 3:
		ponto = ponto/2
	if n[i] == 4:
		ponto= ponto/4
	i+=1
soma= sum(ponto)

print(round(soma,2))
	