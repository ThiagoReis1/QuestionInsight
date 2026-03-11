from numpy import*
n = int(input("number: "))
vect = arange(n+1)
k = n+3

for i in vect:
	if i >= 3:
		nono = vect[k]
		print(nono)
	k = k - 1
print("Fim da contagem regressiva!")
