string = input("Dgite uma string: ")

string = string.upper()

contagem_c = 0

for letra in string:
		if letra == 'C':
			contagem_c +=1
print(contagem_c)