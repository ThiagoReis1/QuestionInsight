# faça seu código aqui!
n = int(input())
c = 0
A = 0
B = 0
C = 0

while c < n:
	t = input().upper()
	c = c + 1
	if t == "A":
		A += 1
	elif t == "B":
		B += 1
	elif t == "C":
		C += 1
print("A=", A)
print("B=", B)
print("C=", C)