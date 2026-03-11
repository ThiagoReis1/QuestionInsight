D = 2.25
S = 4.00
I = 6.90

i = 0
s = input("string: ")
compra = 0
while(i < len(s)):
	if(s[i] == "D"):
		compra = compra + D
	if(s[i] == "S"):
		compra = compra + S
	if(s[i] == "I"):
		compra = compra + I
	i = i + 1
print(round(compra, 2))