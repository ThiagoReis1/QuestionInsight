from numpy import*
valores = array(eval(input("DIGITE VALORES DOS PRODUTOS: ")))
i = 0
while(valores[i] > 80):
	valores[i] = valores[i] - (valores[i]*15/100)
	i = i + 1
print(round(sum(valores), 2))