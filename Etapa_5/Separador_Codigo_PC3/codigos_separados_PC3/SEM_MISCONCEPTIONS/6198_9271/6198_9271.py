ap = float(input("Digite a altura da pessoa: "))
tcp = float(input("Digite a taxa de crescimento da pessoa: "))
al = 1.65
tcl = 0.02
a = 0
y = 0
x = 0
while ap > al:
	a = a +
	y = al + (al * tcl) * a
	x = ap + (ap * tcp) * a
	print(x)