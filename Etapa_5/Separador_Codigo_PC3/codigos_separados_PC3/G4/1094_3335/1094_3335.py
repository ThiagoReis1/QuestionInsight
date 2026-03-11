num = int(input("Insira seu numero: "))

p1 = num // 1000 #primeira metade do numero
r1 = num % 1000
p2 = r1 #segunda metade do numero

eq = (p1+p2)**2

if(eq == num):
	print("atende", num)
else:
	print("nao atende", num)
