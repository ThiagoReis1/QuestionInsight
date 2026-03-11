# faça seu código aqui!
n = int(input())
c = 1
s = 0
while n > c:
	c = c + 1
	if c % 2 == 0:
		s = c + s
print("soma=", s)