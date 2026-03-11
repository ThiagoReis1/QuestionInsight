from numpy import*
pontos= 10000
ond= array(eval(input()))
i=0

while i< size(ond):
	if ond[i] == 1:
		pontos= pontos*2
	elif ond[i] == 2:
		pontos= pontos
	elif ond[i] == 3:
		pontos= pontos / 2
	elif ond[i] == 4:
		pontos= pontos / 4
	i=i + 1
print(round(pontos, 2))