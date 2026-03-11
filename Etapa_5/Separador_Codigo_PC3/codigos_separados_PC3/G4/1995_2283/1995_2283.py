a = input("Qual é o Aminoácido?: ")

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if (a == "Aspartato".lower()):
	p = ((C*4) + (H*6) + (N*1) + (O*4))
	print(round(2, p))
elif(a == "Cisteina".lower()):
	p = ((C*3) + (H*7) + (N*1) + (O*2) + (S*1))
	print(round(2, p))
elif(a == "Metionina".lower()):
	p = ((C*5) + (H*11) + (N*1) + (O*2) + (S*1))
	print(round(2, p))
else:
	print("Entrada:", "p".lower())
	print("Dado Invalido")
