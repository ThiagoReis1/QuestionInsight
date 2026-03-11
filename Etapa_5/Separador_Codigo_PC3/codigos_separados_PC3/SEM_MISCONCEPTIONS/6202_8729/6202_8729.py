altura_bia = 1.69
taxa_bia = 0.01

a = float(input("altura: "))
tx = float(input("taxa: "))

ano = 0

while a <= altura_bia:
	altura_bia += taxa_bia
	a += tx
	ano += 1
	
print(ano)