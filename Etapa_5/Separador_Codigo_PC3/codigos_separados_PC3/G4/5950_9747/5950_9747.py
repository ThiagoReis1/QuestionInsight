a = input("T ou P")
qua = int(input("Quantidade:"))
qu = int(input("Quantidade de cappuccinos"))
if a=="P":
	tot = qua*5+qu*4.5
else:
	tot = qua*6+qu*4.5
print(round(tot,2))