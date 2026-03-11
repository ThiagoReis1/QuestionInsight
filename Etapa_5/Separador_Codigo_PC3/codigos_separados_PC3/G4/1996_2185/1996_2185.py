from math import *

nome = input("aminoacido: ")
O  = 15.9994
C  = 12.011
N  = 14.0067
S  = 32.066
H  = 1.0079

if(nome.lower() == "aspartato"):
	print(round(C*4 + H*6 + N*1 + O*4, 2))
elif(nome.lower() == "fenilalanina"):
	print(round(C*9 + H*11 + O*2 + S*1, 2))
elif(nome.lower() == "tirosina"):
	print(round(C*9 + H*11 + N*1 + O*3, 2))
else:
	print("Entrada: ", nome)
	print("Dado Invalido")