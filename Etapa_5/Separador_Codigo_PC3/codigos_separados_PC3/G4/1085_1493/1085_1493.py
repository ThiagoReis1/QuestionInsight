# UNIVERSIDADE FEDERAL DO AMAZONAS
# AVALIAÇÃO PARCIAL 2
#Michael Evangelista da Cruz
# Engenharia Quimica 
# 07/07/2016

n1 = float(input("Valor da primeira nota: "))
n2 = float(input("Valor da segunda nota: "))
n3 = float(input("Valor da terceira nota: "))
n4 = float(input("Valor da quarta nota: "))
n5 = float(input("Valor da quinta nota: "))

m = ((n1 + n2 + n3 + n4 + n5)/5)

print(round(m, 2)) 
		
if(m >= 6):
	print("Aprovado")
	
else: 
	print("Reprovado")