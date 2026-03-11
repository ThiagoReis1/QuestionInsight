# faça seu código aqui!
n = int(input(""))
c = 0
s = 1

while(s <= n):
	s = (s + 1) ** 2
	c = c + s + 1
n = int(input(""))
print("soma=", c)