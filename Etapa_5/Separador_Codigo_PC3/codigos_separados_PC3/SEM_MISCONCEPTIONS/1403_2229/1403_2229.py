#entradas
A=input("tipo de armadura: ")
D=int(input("destreza: "))

#formula
malha=(15*D)-1
placas=(20*D)-18      

#condicao
if(A.lower()== "malha"):
	resistencia=malha
	
else:
	resistencia=placas
	
print(resistencia)