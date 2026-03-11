from numpy import*

tempo = array(eval(input()))
modo = array(eval(input()))

i = 0
cont=0
while i < size(tempo):
	if modo[i] == "MORNO":
		cont += tempo[i] * 45 * 0.005
	elif modo[i] == "QUENTE":
		cont += tempo[i] * 90 * 0.005
	elif modo[i] == "FRIO":
		cont += tempo[i] * 0 * 0.005
	i= i +1
print(round(cont,2))
		

