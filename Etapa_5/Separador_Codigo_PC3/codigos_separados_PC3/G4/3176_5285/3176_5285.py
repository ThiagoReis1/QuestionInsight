v = str(input("Digite uma palavra: "))

cont = 0

pont = 0

for i in v:
	if i == 'a' or 'e' or 'i' or 'o' or 'u' :
		cont = cont + 1
	else:
		pont = pont + 1
print(cont)
print(pont)