from numpy import*
dado = array(eval(input("Quais os numeros das faces: ")))
i = 0
pts = 200.

while i < size(dado):
	if dado [i] == 1:
	 	pts/= 2
	elif dado [i] == 2:
	 	pts *= 3
	elif dado [i] == 3:
		 pts /= 2
	elif dado [i] == 4:
		pts *= 3
	elif dado [i] == 5:
		pts /=2
	elif dado [i] == 6:
		pts *=3

	i += 1 
print(round(pts,2))