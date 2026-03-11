p = float(input(""))
a = float(input(""))
i = p/(a**2)

if(i<18.5):
	print("abaixo do peso")
if(i>=18.5)and(i<25):
	print("normal")
if(i>=25)and(i<30):
	print("acima do peso")
if(i>30):
	print("obeso")
