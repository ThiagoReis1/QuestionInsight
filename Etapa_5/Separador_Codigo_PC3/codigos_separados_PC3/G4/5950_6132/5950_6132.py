a = input("insira uma opcao (T ou P): ")
b = int(input("quantidade de fatias de torta ou pastel: "))
c = int(input("quantidade de cappuccinos: "))

t = 6              #torta
p = 5              #pastel
cap = 4.5          #cappuccino

if a == "T":
	vt = b*t + c*cap
	print(vt)
else: 
	vt = b*p + c*cap
	print(vt)