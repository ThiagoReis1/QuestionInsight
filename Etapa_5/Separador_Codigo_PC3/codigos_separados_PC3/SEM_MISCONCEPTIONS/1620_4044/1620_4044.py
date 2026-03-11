from numpy import*

temp = array(eval(input("Intervalo de tempo(minutos) dos banhos de Joaozinho: ")))
perc = array(eval(input("Percentual de abertura da torneira: ")))

total = 0
for i in range(size(temp)):
	total += temp[i]*((perc[i]/100)*5)
	
print(round(total, 2))
