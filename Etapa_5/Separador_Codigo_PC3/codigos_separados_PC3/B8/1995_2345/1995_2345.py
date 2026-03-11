Amino=input("Aminoacido:").lower()
O=15.9994
C=12.011
N=14.0067
S=32.066
H=1.00794

Aspartato=C*4+H*6+N+O*4
Cisteina=C*3+H*7+N+O*2+S
Metionina=C*5+H*11+N+O*2+S

if(Amino!="aspartato" and Amino!="cisteina" and Amino!="metionina"):
	print("Entrada:",Amino)
	print("Dado Invalido")
else:
	if(Amino=="aspartato"):
		print(round(Aspartato,2))
	elif(Amino=="cisteina"):
		print(round(Cisteina,2))
	elif(Amino=="metionina"):
		print(round(Metionina,2))