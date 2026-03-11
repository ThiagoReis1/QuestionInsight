from numpy import*

bora = input()
bora = bora.upper()

i = 0
price = 0

while(i < len(bora)):
	if(bora[i] == "A")or(bora[i] == "E")or(bora[i] == "I")or(bora[i] == "O")or(bora[i] == "U"):
		price = price + 45.15
	else:
		price = price + 50.17
	i = i + 1
print(round(price,2))