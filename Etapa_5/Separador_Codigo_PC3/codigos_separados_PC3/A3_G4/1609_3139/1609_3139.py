from numpy import*

x =array(eval(input("top: ").upper()))
y = input("palavra: ")
sn =y.replace("R", "L")
v = ""



cp = 0
cont = 0

while(cp < size(x)):
	if(x[cp] == sn):
		cont = cont + 1
		print(cp)
		cp = cp + 1
else:
	print("NAO ENCONTRADA")



	
	