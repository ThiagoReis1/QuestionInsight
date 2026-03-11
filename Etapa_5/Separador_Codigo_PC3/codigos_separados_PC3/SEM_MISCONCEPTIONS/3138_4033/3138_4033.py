from numpy import*

vet=array(eval(input("Digite os numeros: ")))
i=0
numerador=0
denominador=0

while(i<size(vet)):
	numerador=numerador+(vet[i])**7
	denominador=denominador+1
	i=i+1
print(round((numerador/denominador)**(1/7),2))
	
