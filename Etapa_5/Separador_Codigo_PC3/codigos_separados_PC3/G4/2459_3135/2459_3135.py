p=float(input("Insira o peso ae :"))
d=float(input("Insira a distancia :"))
c=float(input("Insira a cidade :"))

if (c==1):
	print(round(float(p*25 + d*0.10)*(1+17/100),2))
elif(c==2):
	print(round(float(p*25 + d*0.10)*(1+17.5/100),2))
elif(c==3):
	print(round(float(p*25 + d*0.10)*(1+18/100),2))
elif(c==4):
	print(round(float(p*25 + d*0.10)*(1+20/100),2))
else:
	print("Entradas Invalidas")