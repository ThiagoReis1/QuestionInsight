doce = 2.25
salgado = 4
integral = 6.9

entrada = input()

d = 0
s = 0
i = 0
for j in range(len(entrada)):
	if entrada[j] == "D":
		d+=1
	elif entrada[j] == "S":
		s+=1
	elif entrada[j] == "I":
		i+=1
		
total = doce*d + salgado*s + integral*i
		
print(round(total, 2), d, s, i)