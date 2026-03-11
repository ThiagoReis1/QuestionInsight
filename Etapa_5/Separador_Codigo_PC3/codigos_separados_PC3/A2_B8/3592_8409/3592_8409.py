from numpy import*
cont = 100
dados = array(eval(input("valores:")))
for i in range (size(dados)):
	if dados[i] == 1:
		cont = cont
	elif dados[i] == 2:
		cont = cont*2
	elif dados[i] == 3:
		cont = (cont)/3
	elif dados[i] == 4:
		cont = cont*4
	elif dados[i] == 5:
		cont = cont/5
	elif dados[i] == 6:
		cont = cont*6

print(round(cont,2))