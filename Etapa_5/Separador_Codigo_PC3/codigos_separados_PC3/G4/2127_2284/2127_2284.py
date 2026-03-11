from numpy import*

n = array(eval(input()))
m = (n[1] + n[2] + n[3])/3

if (m >= 50):
	print(round(m, 2))
	print("APROVADO")
else:
	print(round(m, 2))
	print("REPROVADO")