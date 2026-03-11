antigo = float (input ("produto antigo:"))
if antigo <=100.00:
	c= antigo + (antigo*(5/100))
	msg= "Aumento de 5 porcento"
else:
	c= antigo + (antigo * (15/100))
	msg = "Aumento de 15 porcento"

print (round(c,2),"ryous")
print (msg)
