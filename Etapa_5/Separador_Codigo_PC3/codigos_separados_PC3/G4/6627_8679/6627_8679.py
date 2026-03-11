# faça seu código aqui!
v = str(input().upper())

i = 0
j = 0
while i < len(v):
	if v[i] == "D":
		j = j + 1
	i = i + 1
print(j)