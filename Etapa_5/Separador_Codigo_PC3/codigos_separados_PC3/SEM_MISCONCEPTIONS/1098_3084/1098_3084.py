n = int(input("numero: ")) 
d1 = n // 1000
resto1 = d1 % n
resto2 = n % d1
if ((resto1 - resto2) ** 4 == n):
	msg = "atende"
else:
	msg = "nao atende"
print(n)
print(msg)