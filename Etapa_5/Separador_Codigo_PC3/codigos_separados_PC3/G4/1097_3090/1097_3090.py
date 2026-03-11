n = int(input("Numero: "))
n1 = (n //1000)
n2 = (n % 1000)
c = (n1 - n2)**2
if	(c == n):
	msg = "atende"
else: 
	msg = "nao atende"
print(msg)
print(n)