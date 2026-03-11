#Universidade Federal do Amazonas 
#Laís Amorim Reis - 21602327

Z = int(input("zumbis: "))
H = int(input("habitantes: "))
X = int(input("pessoas por dia: "))
Y = int(input("zumbis por dia: "))
dias = 0

while(H>0):
	Z = Z*X
	Z = Z - Y
	H = H - Z
	dias = dias + 1
print(dias)
