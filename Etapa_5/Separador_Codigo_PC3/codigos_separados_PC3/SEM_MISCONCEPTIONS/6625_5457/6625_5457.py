# faça seu código aqui!
entrada = input("B").upper()
i = 0
c = 0

while i < len(entrada):
	if entrada[i] == "B":
		c = c + 1
	i = i + 1

print(c)

