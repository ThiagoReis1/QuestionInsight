num = int(input("insira: "))
m = 0 
n = 0
while (num!=0) :
	div = num%2
	if (div ==0) :
		m = m + 1
	else :
		n = n + 1
	z = m + n 
	par = (m/z)*100
	impar = (n/z)*100
	num = int(input("insira: "))
print(round(par, 2))
print(round(impar, 2))