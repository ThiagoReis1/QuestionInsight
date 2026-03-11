p1 = float(input("Digite a nota 1: "))
p2 = float(input("Digite a nota 2: "))
p3 = float(input("Digite a nota 3: "))
media = (p1 + p2 + p3)/3
if(media >= 5):
	print(round(media,1)) 
	print("Aprovado")			
else:
	print(round(media,1))
	print("Reprovado")