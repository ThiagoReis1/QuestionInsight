combustivel = int(input("quantidade de combustivel: "))

if combustivel<17.5:
	total = combustivel +10.5
elif 17.5<combustivel<35:
	total = combustivel + 14
elif 35<combustivel<50:
	total = combustivel + 18.6
else:
	total = combustivel+24.5

print(round(total,2))