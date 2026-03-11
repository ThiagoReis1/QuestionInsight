aminoacido = input()
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794
x = C*4 + H*6 + N + O*4
y = C*3 + H*7 + N + O*2 + S
z = C*5 + H*11 + N + O*2 + S
if(aminoacido == "aspartato".lower()):
	print(round(x,2))
elif(aminoacido == "cisteina".lower()):
	print(round(y,2))
elif(aminoacido == "metionina".lower()):
	print(round(z,2))
else:
	
	print("Dado Invalido")