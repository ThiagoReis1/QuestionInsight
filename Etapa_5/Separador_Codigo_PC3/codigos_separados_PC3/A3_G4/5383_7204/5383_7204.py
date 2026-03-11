s = input("etiqueta: ")

i = 0
j = 0
t = 0
while i < len(s):
	if s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
		j = j + 1
	i = i + 1
	
c = j*0.12 + (i-j)*0.18

print(round(c,2))