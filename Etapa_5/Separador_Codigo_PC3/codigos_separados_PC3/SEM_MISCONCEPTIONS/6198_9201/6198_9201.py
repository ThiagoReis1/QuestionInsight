altura_luna = 1.65
taxa_luna = 0.02
anos = 0 

ma = float(input("digite:"))
tm = float(input("digite:"))
cresl = 1.65
cresa = ma

while(cresl>cresa):
	cresl = altura_luna + taxa_luna*anos
	cresa = ma + tm*anos  
	anos +=1
print(anos-1)
