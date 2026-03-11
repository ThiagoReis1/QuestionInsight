uni = input("qual e a unidade: ")
val = float(input("qual o valor da medida: "))

if uni == "O":
	k = val/35.274 
	print(round(k, 2))
else:
	o = 35.274 * val 
	print(round(o, 2)) 