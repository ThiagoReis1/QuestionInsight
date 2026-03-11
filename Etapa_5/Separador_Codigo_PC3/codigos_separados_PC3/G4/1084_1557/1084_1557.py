p1 = float(input("Digite a prova 1: "))
p2 = float(input("Digite a prova 2: "))
p3 = float(input("Digite a prova 3: "))
p4 = float(input("Digite a prova 4: "))
media = (p1+p2+p3+p4)/4
print(round(media, 1))
if (media >= 6.0):
		 print ("Aprovado")
else:
		 print ("Reprovado")