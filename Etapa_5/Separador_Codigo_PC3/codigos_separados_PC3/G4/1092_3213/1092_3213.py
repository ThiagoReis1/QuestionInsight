nu = int(input("Digite o numero: "))

a1 = nu // 100
a2 = (nu % 100) // 10
a3 = ((nu % 100) % 10) // 1

#print(a1)
#print(a2)
#print(a3)

ca = (a1 ** 3) + (a2 ** 3) + (a3 ** 3)
#print(ca)

if (ca == nu):
	si = "atende"
else:
	si = "nao atende"

print(nu)
print(si)