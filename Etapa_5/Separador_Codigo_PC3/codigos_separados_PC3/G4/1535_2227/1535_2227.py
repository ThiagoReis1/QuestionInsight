from math import*
angx=int(input("sentido radiano: "))
k=int(input("termo serie: "))
soma=0
cont=1

while(cont<k):
	soma=soma+1((angx**3((cont*2))))/(factorial*(cont*2))*((-1**cont))
	cont=cont+1

print(round(soma,6))