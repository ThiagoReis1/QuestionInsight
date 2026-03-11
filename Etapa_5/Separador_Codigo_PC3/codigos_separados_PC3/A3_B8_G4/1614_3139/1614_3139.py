from numpy import* 

a = array(input("alimentos: ").upper())
k = array(eval(input("quantidade de gramas: ")))



if (a == "BANANA"):
	x = k * 0.97
elif (a == "BIFE"):
	x = k * 2.95
elif (a == "FEIJOADA"):
	x = k * 1.27
elif(a == "OMELETE"):
	x = k * 1.04
elif(a == "TOMATE"):
	x = k * 0.2
print(round(k, 2))