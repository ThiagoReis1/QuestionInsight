# Mayume Ihara Lima Rodrigues - 21602330
# Avaliacao 2
# Exercicio 1
# 14 / 07/ 2016

n1 = float(input("nota 1: "))
n2 = float(input("nota 2: "))
n3 = float(input("nota 3: "))
n4 = float(input("nota 4: "))
n5 = float(input("nota 5: "))

media = (n1 + n2 + n3 + n4 + n5)/ 5
print(round(media, 2))
if(media >= 6):
		print("Aprovado")
else:
		print("Reprovado")