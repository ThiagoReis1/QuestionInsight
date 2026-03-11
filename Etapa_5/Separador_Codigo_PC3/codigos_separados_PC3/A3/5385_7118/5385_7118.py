from numpy import*

letra = input().upper()

vogal = 35.15
consoante = 42.17
i = 0
cont = 0
acum = 0
while i < len(letra):
	if letra[i] == "A" or letra[i] == "E" or letra[i] == "I" or letra[i] == "O" or letra[i] == "U":
		acum = acum + vogal
	else:
		acum = acum + consoante
	
	i = i + 1
print(round(acum, 2))
