from numpy import*

m = input("digite a palavra: ").lower()
v1 = len(m)
i = 0

while (i < v1):
	if (m[i] == "m"):
		print(i)
	i += 1
if ("m" not in m):
	print("nao achei")
	


