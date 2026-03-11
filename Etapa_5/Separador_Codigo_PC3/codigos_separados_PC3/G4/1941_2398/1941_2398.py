op = input("Digite  opcao(glicina ou serina): ")
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079
if (op.upper() == "GLICINA"):
	pm = (c*2)+(h*5)+n+(o*2)
	print(round(pm, 2))
if (op.upper() == "SERINA"):
	pm = (c*3)+(h*7)+n+(o*3)
	print(round(pm, 2))