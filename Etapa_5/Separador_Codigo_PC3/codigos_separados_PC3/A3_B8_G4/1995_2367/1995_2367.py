X = input("Nome do aminoacido:").lower()

O = 15.994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(X!="aspartato" and X!="cisteina" and X!="metionina"):
	X = "Dado invalido"
	print(X)

elif(X == "aspartato"):
 	X = 4*o + 6*h + n + 4*o
 
elif(X == "cisteina"):
 	X = 3*o+7*h+n+2*o+s
elif(X == "metionina"):
	X = 5*c+11*h+n+2*o+s

print(round(X,2))