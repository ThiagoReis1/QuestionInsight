net = int(input("digite velocidade da net: "))
plano = 60.0
if net < 50: 
	total = plano + 4.50
elif net == 50 :
	total = plano + 5.50
else: 
	total = plano + 6.50
print("total=",(round(total, 2)))
