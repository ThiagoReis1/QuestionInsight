n1 = float(input("qual o valor da nota 1: "))
n2 = float(input("qual o valor da nota 2: "))
n3 = float(input("qual o valor da nota 3: "))

media = n1 / 3 + n2 / 3 + n3 / 3

print(round(media , 1))

if(media >= 5.0 ):
	print("Aprovado")
	
else:
	print("Reprovado")
	

	