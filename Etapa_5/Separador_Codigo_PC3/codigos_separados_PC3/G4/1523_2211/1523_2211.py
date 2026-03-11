#Quantidade inicial
a = int(input("Quantidade inicial: "))
#Novos balões lançados
b = int(input("Quantidade de novos balões: "))
#Balões destruidos
c = int(input("Quantidade de balões destruidos: "))
#semanas
t=0
while (a<200):
	a = a + b - c
	t = t + 1
print (t)
	
	
	
	
	
	
	