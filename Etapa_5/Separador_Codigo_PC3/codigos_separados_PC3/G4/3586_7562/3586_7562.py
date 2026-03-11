from numpy import*

a = array(eval(input("Insira a quant de acertos: ")))
x = 0
i = 0

while i < size(a):
	if a[i] == 1:
		x = x+ 100
	if a[i] == 2:
		x =x+ 60
	if a[i] == 3:
		x = x + 20
	
	i += 1
	
	
print(x)