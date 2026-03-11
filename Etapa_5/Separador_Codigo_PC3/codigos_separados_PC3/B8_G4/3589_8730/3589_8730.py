from numpy import*
num = array(eval(input("alvos acertados:")))
i = 0
cont = 0
while i < size(num):
	if num[i]==1:
		cont = cont+80
	elif num[i] ==2:
		cont = cont+40
	elif num[i] ==3:
		cont = cont+20
	elif num[i] ==4:
		cont = cont+10
	i = i + 1
print(round(cont,2))