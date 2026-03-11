from numpy import*
tempo = array(eval(input(" ")))
abertura = array(eval(input(" ")))
i = 0
consumo = 0

while(i < size(tempo)):
	consumo = consumo + tempo[i] * ( 5 * abertura[i]/100)
	i = i + 1



print(round(consumo,2))
