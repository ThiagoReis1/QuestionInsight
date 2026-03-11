# Monalisa Pereira 21600560
# 280716
# Av 04 - Ex 02

N = int(input("Informe o número de termos para a série: "))

S = (1**3)/(5+1)
x = 2
y = 3
c = 1

while (c<N):
	if (c%2!=0):
		S = S - (x**3)/(5+y)
	else:
		S = S + (x**3)/(5+y)
	x = x+1
	y = y+2
	c = c+1

print(round(S,9))