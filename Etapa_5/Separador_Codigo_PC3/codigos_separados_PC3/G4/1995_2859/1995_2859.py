am = input("Nome do Aminoacido: ")

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

if(am.lower() == "aspartato"):
	pm = (c*4+h*6+n+o*4)
	print(round(pm,2))
elif(am.lower() == "cisteina"):
	pm = (c*3+h*7+n+o*2+s)
	print(round(pm,2))
elif(am.lower() == "metionina"):
	pm = (c*5+h*11+n+o*2+s)
	print(round(pm,2))
else:
	print("Entrada: ",am.lower())
	print("Dado Invalido")
