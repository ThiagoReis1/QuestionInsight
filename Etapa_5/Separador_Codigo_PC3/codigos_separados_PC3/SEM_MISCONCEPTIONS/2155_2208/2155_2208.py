from numpy import*

peso=array(eval(input("Peso da Turma: ")))
altura=array(eval(input("Altura da Turma: ")))

imc=peso/(altura*altura)
print(imc)

if(imc<17):
	a1="MUITO ABAIXO DO PESO"
elif(imc>=17 and <=18.49):
	a1="ABAIXO DO PESO"
elif(imc>=18.50 and <=24.99):
	a1="PESO NORMAL"
elif(imc>=25 and <=29.99):
	a1="ACIMA DO PESO"
elif(imc>=30 and <=34.99):
	a1="OBESIDADE"
elif(imc>=35 and 39.99):
	a1="OBESIDADE SEVERA"
elif(imc>40):
	a1="OBESIDADE SEVERA"


x=0

for i in range (size(imc)):
	if(tur[i]%3==0):
		x = x +1
	
vet=zeros(x, dtype = int)
print(x)
y=0
for i in range(size (tur)):
	if(tur[i]%3==0):
		vet[y]=i
		y=y+1
		
print(vet)








print(max(saida))