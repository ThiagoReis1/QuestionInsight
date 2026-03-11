s = int(input("digite um numero: "))
print(s)

d1 = s // 10000

d2 = s % d1 

cal = (d1 + d2) ** 2

if (cal == s):
	msg = "atende"
else:
	msg = "nao atende"

print(msg)