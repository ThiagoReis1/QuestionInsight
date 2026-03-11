# faça seu código aqui!
s = input("str: ").upper()
i = 0
m = 0
while i < len(s):
	if s[i] == "M":
		print(i)
		m += 1
	i = i +1
if m == 0:
	print("nao achei")