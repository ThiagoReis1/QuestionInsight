n = int(input(""))

d1 = n//100
d2 = n//10%10
d3 = n%10
d4 = n//100
d5 = n//10%10
d6 = n%10

m = d1+d2+d3
o = d4+d5+d6 


if ((m+o)**2 == n):
    mensagem = "atende"
else:
	 mensagem = "nao atende"
print(mensagem)
print(n)	
		
