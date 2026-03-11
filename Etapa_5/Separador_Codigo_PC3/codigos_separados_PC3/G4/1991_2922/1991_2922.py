a = input ("Aminoacido: ")
c = 12.011
h = 1.0079
n = 14.00674
o = 15.9994
g = c * 2 + h * 5 + n *1 + o * 2
p = c * 5 + h * 10 + n *1 + o * 2
s = c * 3 + h * 7 + n *1 + o * 3
if (a.lower() == "glicina"):
	print (round(g,2))
elif (a.lower() == "prolina"):
	print (round(p,2))
elif (a.lower() == "serina"):
	print (round(s,2))
else:
	print ("Entrada:", a)
	print ("Dado Invalido")