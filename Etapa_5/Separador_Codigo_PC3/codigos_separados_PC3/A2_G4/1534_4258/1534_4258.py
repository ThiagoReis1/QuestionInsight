x = float(input("Numero real x: "))
k = int(input("Quantidade de termos das serie: "))

n = k
s = x
p = 1

if(k == 1):
	s = s
	
while(n != 1):

	s = s + ((x**(2*p + 1))/(2*p + 1))
	n = n - 1
	if(n != 1):
		p = p + 1
		
print(round(s, 7))