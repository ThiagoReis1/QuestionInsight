n = int(input("Digite o numero:")) 
c1 = n//10000
c2 = n%10000
op = (c1+c2)**2
if (n)==op:
	msg = "atende"
else:
	msg = "nao atende"
print (n)
print (msg)