
qi = int(input("mana inicial:"))
qg= int(input("gasta:"))
qr= int(input("recupera:"))

t= 0
q= qi

while(q > 0):
	q=  q - qg + qr
	t= t+1
print(t)