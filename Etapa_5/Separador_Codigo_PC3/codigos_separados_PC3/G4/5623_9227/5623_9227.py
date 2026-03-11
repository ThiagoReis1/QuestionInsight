x = input("comida B ou S:")
z = int(input("quantidade de fatias de bolo ou salgado:"))
y = int(input("quantidade de capuccinos:"))
if(x.upper() == "B"):
	total = z*5 + y*7.50

else:
	total = z*4 + y*7.50

print(total)