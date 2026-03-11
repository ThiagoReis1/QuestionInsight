from numpy import * 

num = array(eval(input("numeros: ")))

ind = 0
pontos = 0

while ind < size(num):
	if num[ind] == 1:
		pontos = pontos + 10
	elif num[ind] == 2:
		pontos = pontos + 5
	elif num[ind] == 3:
		pontos = pontos + 10
	elif num[ind] == 4:
		pontos = pontos + 5
	elif num[ind] == 5:
		pontos = pontos + 10 
	elif num[ind] == 6:
		pontos = pontos + 5
	ind = ind + 1
print (pontos)