p1 = float(input ("diite o valor da p1: "))
p2 = float(input ("diite o valor da p2: "))
p3 = float(input ("diite o valor da p3: "))
p4 = float(input ("diite o valor da p4: "))
p5 = float(input ("diite o valor da p5: "))
med = (p1+p2+p3+p4+p5)/5
print (round(med,1))
if (med >= 5):
	print("Aprovado")
else:
	print ("Reprovado")