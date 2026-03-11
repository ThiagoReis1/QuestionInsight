cor = input("cor da casa")
cor = cor.upper()
cont =0
while cor != "S":
	if cor =="PRETA":
		cont = cont +1
	cor = input("cor da casa")
	cor = cor.upper()

print (cont)