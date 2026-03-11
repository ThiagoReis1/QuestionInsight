a = input("Aminoacido: ")

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(a == "Cisteina".lower()):
	c = ((C*3)+(H*7)+(N)+(O*2)+(S))
	print(round(c, 2))
elif(a == "Isoleucina".lower()):
	c = ((C*6)+(H*13)+(N)+(O*2))
	print(round(c, 2))
elif(a == "Metionina".lower()):
	c = ((C*5)+(H*11)+(N)+(O*2)+(S))
	print(round(c, 2))
else:
	print("Entrada:", a)
	print("Dado Invalido")