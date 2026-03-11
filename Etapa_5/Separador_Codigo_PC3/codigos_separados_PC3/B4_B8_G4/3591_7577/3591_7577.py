from numpy import*

dado = array(eval(input("Jogue o dado: ")))

i=0
ponto = 0

while i < size(dado):
	if dado[i] == 1: 
		ponto += 10
	elif dado[i] == 2:
		ponto += 5
	elif dado[i] == 3:
		ponto += 10
	elif dado[i] == 4:
		ponto += 5
	elif dado[i] == 5:
		ponto += 10
	elif dado[i] == 6: 
		ponto += 5
	soma = ponto
	i=i+1
print(soma)