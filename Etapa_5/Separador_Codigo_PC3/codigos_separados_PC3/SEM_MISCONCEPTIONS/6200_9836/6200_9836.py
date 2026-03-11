altura_max = 1.75
taxa_max = 0.01

altura=float(input("altura:"))
taxa=float(input("taxa:"))

ano=0

while (altura < altura_max) :
	altura_max = altura_max + taxa_max
	altura = altura + taxa
	ano += 1
	
print (ano)

