from math import *
nome = input("nome do aminoacido (Aspartato ou Cisteina): ")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

Aspartato = C * 4 + H * 6 + N * 1 + O * 4
Cisteina = C * 3 + H * 7 + N * 1 + O * 2 + S

if(nome.lower() == "aspartato"):
	print(round(Aspartato,2))
if(nome.lower() == "cisteina"):
	print(round(Cisteina,2))
