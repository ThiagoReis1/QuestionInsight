
s = input("Digite uma frase: ")
x = len(s)

consoante = 0
vogal = 0

for i in range(0,x):
	if (s[i] == "a"):
		vogal = vogal + 1
	elif (s[i] == "e"):
		vogal = vogal + 1
	elif (s[i] == "i"):
		vogal = vogal + 1
	elif (s[i] == "o"):
		vogal = vogal + 1
	elif (s[i] == "u"):
		vogal = vogal + 1
	else:
		consoante = consoante + 1
		
print(vogal)
print(consoante)