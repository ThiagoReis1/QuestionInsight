from numpy import*
pontos = array(eval(input("digite a entrada: ")))

comp = 200
i=0


anel1 = comp*4
anel2 = comp*2
anel3 = 3
anel4 = comp/2

print(pontos)

while(i<=size(pontos)):
	if(pontos[i] == 1):
		comp = comp*4
	elif(pontos[i] == 2):
		comp = comp*2
	elif(pontos[i] == 3):
		comp = 3
	else:
		comp = comp/2
	
print(comp)
	