#Peso molecular

aminoacido = input("aspartato, cisteina ou metionina? ").lower()

O= 15.9994
C = 12.011
N = 14.0067
S=32.066
H = 1.00794

if(aminoacido!="aspartato") and (aminoacido!="cisteina") and(aminoacido!="metionina"):
	print("Entrada:",aminoacido)
	print("Dado Invalido")
	
elif(aminoacido=="aspartato"):
	peso= (C*4)+(H*6)+(N*1)+(O*4)
	print(round(peso,2))
elif(aminoacido=="cisteina"):
	peso= (C*3)+(H*7)+(N*1)+(O*2) + (S*1)
	print(round(peso,2))
elif(aminoacido=="metionina"):
	peso= (C*5)+(H*11) +(N*1)+(O*2) + (S*1)
	print(round(peso,2)) 




	