a = float(input("peso:"))
b = float(input("Distancia:"))
c = float(input("Codigo:"))

if(c==1):
	S = (a*25 + b*0.10)*(1.0+17.0/100)
	print(round(S, 2))
elif(c==2):
	S = ((a*25) + (b*0.10))*(1.0+(17.5/100))
	print(round(S, 2))
elif(c==3):
	S = ((a*25) + (b*0.10))*(1.0+(18.0/100))
	print(round(S, 2))
elif(c==4):
	S = ((a*25) + (b*0.10))*(1.0+(20.0/100))
	print(round(S, 2))