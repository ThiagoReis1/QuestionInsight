from numpy import*

coef=array(eval(input("Digite os coeficientes do polinomio: ")))

i=0
poli=""

while(i<size(coef)):
	if(i-1!=-1):
		poli=poli+str(coef[i])+ "x^ + " + str(1*(i+1))
		num=coef[-1]
	i=i+1
print(poli+str(num))

#nao 