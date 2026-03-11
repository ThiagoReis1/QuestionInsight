from numpy import*
tempo = array(eval(input("Tempo: ")))

i = 0
while(tempo[i] > min(tempo)):
	i = i + 1
print(i)