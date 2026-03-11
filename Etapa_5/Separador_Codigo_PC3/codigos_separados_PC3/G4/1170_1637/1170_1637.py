#Universidade Federal do Amazonas
#Aluna:Ingrid de Lira Lima
#Questão: 2 

n=int(input("digite um numero:"))
va = 0
vc = 1

while(vc < n):
	den= 1+(2+vc*2)
	va = va+ (vc+1)*(-1)**(vc+2)/ den
	vc=vc+1
print(round(va,7))