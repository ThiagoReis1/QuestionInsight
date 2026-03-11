from math import *
e = float(input())
f = float(input())
print("Entradas:", e, "horas extras e", f, "horas de falta")
H = round((e - ((2/3)*f)), 2)
if (e<0) or (f<0):
	print("Dados invalidos")
elif H > (2400):
	G = 500
	print("Gratificacao: R$", G)
elif 1800< H <= (2400):
	G1 = 400
	print("Gratificacao: R$", G1)
elif 1200 < H <= (1800):
	G2 = 300
	print("Gratificacao: R$", G2)
elif 600< H <= (1200):
	G3 = 200
	print("Gratificacao: R$", G3)
elif H <= (600):
	G4 = 100
	print("Gratificacao: R$", G4)