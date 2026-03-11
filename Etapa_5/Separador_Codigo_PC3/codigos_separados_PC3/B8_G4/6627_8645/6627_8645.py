# faça seu código aqui!

v=input("v: ").upper()
i = 0
e = 0
while i < len(v):
	if v[i] == "D":
		i = i + 1
		e = e + 1
	elif v[i] != "D":
		i = i + 1
		e = e + 0	
print(e)		