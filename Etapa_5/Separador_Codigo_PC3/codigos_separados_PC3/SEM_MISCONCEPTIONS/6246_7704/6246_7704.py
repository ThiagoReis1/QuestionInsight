from numpy import*

vitorias= input().upper()

vit=0

while vitorias!= "X":
	if vitorias== "A":
		vit+=1
	vitorias= input().upper()
	
print(vit)