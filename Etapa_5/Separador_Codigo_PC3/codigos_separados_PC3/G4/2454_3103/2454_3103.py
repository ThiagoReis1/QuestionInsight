h = float(input("Qual a sua altura(em metros)?: "))
s = (input("Qual seu sexo?:").upper())
H = (72.7 * h) - 58
M = (62.1 * h) - 44.7
if(h < 1 or h > 2.5): 
	print("altura invalida")
elif(s != "M" and s != "F"):
	print("codigo invalido de sexo")
elif(s == "M"):
	print(round(H,2))
else:
	print(round(M,2))