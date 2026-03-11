x = float(input("Altura da pessoa: "))
y = float(input("Taxa de crescimento: "))
altura_bia = 1.69
taxa_bia = 0.01
ano = 0

while(altura_bia > x):
	altura_bia = altura_bia + taxa_bia
	x = x + y
	ano = ano + 1
		
		
print(ano)	
		

