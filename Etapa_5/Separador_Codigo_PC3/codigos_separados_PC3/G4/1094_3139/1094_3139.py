x = int(input("numero: "))

c = (x // 1000)
e = (x % 1000) 

F = (c + e) ** 2

if (F == x):
	msg = "atende"
else:
	msg = "nao atende"
	
print(msg)
print(x)




