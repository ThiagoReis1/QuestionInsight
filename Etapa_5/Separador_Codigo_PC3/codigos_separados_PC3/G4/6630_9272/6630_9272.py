a = input("plavavra").upper()
i = 0
c = 0
while i < len(a):
	if a[i] == "L":
		c = c + 1
		print(i)
	i = i + 1
if c == 0:
	print("nao achei")