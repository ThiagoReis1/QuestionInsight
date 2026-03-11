from numpy import*

notas = array(eval(input("Notas finais: ")))

acum = 0

for i in range(size(notas)):
	if notas[i] < 5:
		acum = acum + 1
print (acum)

vcont = zeros(acum, dtype = int)
k = 0

for i in range(size(notas)):
	if notas[i] < 5:
		vcont[k] = i
		k = k + 1
print(vcont)
