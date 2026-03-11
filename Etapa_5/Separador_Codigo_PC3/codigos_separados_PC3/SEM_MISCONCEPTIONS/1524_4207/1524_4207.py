inicial= int(input("Insira a quantidade de grifos: "))
x= int(input("Insira a quantidade de grifos treinados: "))
y= int(input("Insira a quantidade de grifos contaminados a cada semestre: "))

grifos= 0
i=0

while(i<400):
	grifos= (inicial - y) - x 
	i= i + 1
	if(grifos==0):
print(grifos)