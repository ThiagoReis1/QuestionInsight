s = input("Digite a sequencia: ").upper()

i = 0
x = 0
while i < len(s):
	if s[i] == "B":
		x +=  6.80
	elif s[i] == "C":
		x +=  11.75
	elif s[i] == "M":
		x +=  5.90
	i = i + 1
print(round(x,2))