# Aluna: Lizandra Kamila Muniz de Andrade - 21553759
# Universidade Federal do Amazonas - UFAM
# 14/07/16
p1 = float(input("insira a primeira nota: "))
p2 = float(input("insira a segunda nota: "))
p3 = float(input("insira a terceira nota: "))
p4 = float(input("insira a quarta nota: "))
ma = (p1 + p2 + p3 + p4)/4
if (ma>=7):
	print(round(ma,2))
	print("Aprovado")
else:
	print(round(ma,2))
	print("Reprovado")