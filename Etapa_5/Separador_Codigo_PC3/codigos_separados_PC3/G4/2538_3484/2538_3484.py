s = float(input())
d = float(input())
m = float(input())
j = float(input())

cont = 0
inicial = s

if s > 0 and d > 0 and m > 0 and j > 0:
	while inicial < (m + (m * 0.1)):
		s = round((s + (s * (d/100)) - m),2)
		cont = cont + 1
		m = float(input())
	print(cont)
else:
	print ("Dados incorretos")
	
		