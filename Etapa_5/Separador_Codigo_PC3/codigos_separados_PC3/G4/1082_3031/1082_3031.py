a = float(input("primeira nota"))
b = float(input("segunda nota"))
c = float(input("terceira nota"))
d = float(input("quarta nota"))
e = float(input("quinta nota"))


med = (a + b +c +d + e) / (5.0)
# arredondamento 

print(round(med,1))


#condicao
if (med >= 5.0):
	print ("Aprovado")
	
else:
	print ("Reprovado")


