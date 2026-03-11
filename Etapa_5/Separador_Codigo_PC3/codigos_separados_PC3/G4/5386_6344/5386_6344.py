from numpy import*

s = input("Digite a senha: ")

i = 0
acum = 0

while i < len(s):
	if s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
		acum = acum + 1.12
	else:
		acum = acum + 1.18
	i = i + 1
	
print(round(acum ,2))