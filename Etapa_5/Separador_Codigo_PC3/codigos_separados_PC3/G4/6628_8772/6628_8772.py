# faça seu código aqui!
s = input().upper()
i = 0
e = 0

while i < len(s):
	if s[i] == "E":
		e = e + 1
	i = i + 1
print(e)	
