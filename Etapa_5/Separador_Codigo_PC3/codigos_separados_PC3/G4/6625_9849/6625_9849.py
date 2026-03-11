# faça seu código aqui!
s = str(input("")).upper()
c = 0
l = len(s)

for i in range(l):
	if s[i] == "B":
		c += 1

print(c)