from numpy import*

dados = array(eval(input("Quais os resultados obtidos: ")))
i = 0
acm = 0

while i < size(dados):
	if dados[i] == 1:
		acm = acm + 10
	elif dados[i] == 2:
		acm = acm + 5
	elif dados[i] == 3:
		acm = acm
	elif dados[i] == 4:
		acm = acm + 5
	elif dados[i] == 5:
		acm = acm + 20
	elif dados[i] == 6:
		acm = acm + 10
	i += 1
	
print(acm)