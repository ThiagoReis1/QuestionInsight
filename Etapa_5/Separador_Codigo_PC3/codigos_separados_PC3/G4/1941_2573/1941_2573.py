nome = input("digite glicina ou serina: ")
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
if (nome.upper() == "GLICINA"):
	peso = c*2+h*5+n+o*2
else:
	peso= c*3+h*7+n+o*3
print(round(peso, 2))


