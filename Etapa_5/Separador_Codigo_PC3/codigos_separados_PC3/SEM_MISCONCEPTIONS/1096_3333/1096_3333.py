num=int(input("leia o numero de entrada"))
d1=num//10000
print(d1)
d2=num//100-d1*100
print(d2)
d3=num//100-
print(d3)
c=d1**3+d2**3+d3**3
if	(num == c):
	mensagem= "atende"
else:
	mensagem= "nao atende"
print(mensagem)
print(c)