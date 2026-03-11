p = float(input("preco: "))
r = int(input("regiao: "))

if (r == 1):
	f = p*0.1
elif(r == 2):
	f = p*0.08
elif(r == 3):
	f = p*0
else:
	f = p*0.02
	
vv = (p - (0.40*p))+ (p*(f/100))
print(round(vv,2))