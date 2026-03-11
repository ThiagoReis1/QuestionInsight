from numpy import *
num = array(eval(input("dados lançados: ")))

i=0
cont=200

while i < size(num):
	if num[i]==1:
		cont=cont/2
	elif num[i]==2:
		cont=cont*3
	elif num[i]==3:
		cont=cont/2
	elif num[i]==4:
		cont=cont*3
	elif num[i]==5:
		cont=cont/2
	elif num[i]==6:
		cont=cont*3
	i=i+1
print(round(cont,2))