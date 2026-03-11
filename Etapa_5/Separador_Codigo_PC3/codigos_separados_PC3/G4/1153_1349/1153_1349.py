patP=float(input("Qual patrimonio do Pobresco? "))
patB=float(input("Qual patrimonio do Bitcoin? "))
perP=float(input("Qual percentual do Pobresco? "))/100
perB=float(input("Qual percentual do Bitcoin? "))/100
i=1

while patB<patP:
	patP+=patP*perP
	patB+=patB*perB
	i+=1
	
print(i)