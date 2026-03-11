m = input("") #molecula 
mp = m.upper()

o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
if(mp == "ALANINA"):
	pm = 3*c + 7*h + n + 2*o
	print(round(pm, 2))
elif(mp == "VALINA"):
	pm = 5*c + 11*h + n + 2*o
	print(round(pm, 2))
elif(mp == "TIROSINA"):
	pm = 9*c + 11*h + n + 3*o
	print(round(pm, 2))
else:
	print("Entrada: ", m) #problema
	print("Dado Invalido")
