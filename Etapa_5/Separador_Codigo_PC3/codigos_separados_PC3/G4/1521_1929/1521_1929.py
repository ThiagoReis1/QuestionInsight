n = int(input("capacidade N do navio: "))
e = int(input("estoque inicial: "))
q = int(input("quantidade Q: "))
s = 0
while (e > 0):
	e = e - n + q
	s = s +1
print(s)
