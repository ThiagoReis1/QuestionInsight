from numpy import *
n = input(": ")
if(len(n) == 11):
	j = 0
	novo = ""
	for i in range(len(n)):
		if(i == 1):
			novo = novo + n[i]
		elif(i == 3):
			novo = novo + (n[i])
		elif(i == 5):
			novo = novo + (n[i])
		elif(i == 7):
			novo = novo + (n[i])
		elif(i == 9):
			novo = novo + (n[i])
	print(novo)
else:
	print("INVALIDO")