from numpy import*
vetor=array(eval(input("digite o vetor:  ")))
for i in vetor:
	if i>80:
		i=i-(i*0.15)
print(i)