n = int(input("numero:"))

a1 = n//100
a2 = n%100

if(a1**2 + a2**2 == n):
	print("atende")
else:
	print("nao atende")

print(n)



