from numpy import*

entrada = input("")

i = 0
soma = 0
c1= 0
c2 = 0
c3 = 0
while i < len(entrada):
	if entrada[i] == "H":
		c1 = c1 + 1
		soma = soma + 5.40
	elif entrada[i] == "C":
		soma = soma + 8.95
		c2 = c2 + 1
	elif entrada[i] == "L":
		soma = soma + 4.50
		c3 = c3 + 1
	i = i + 1
total = round(soma,2)
print(total, c1,c2,c3)
