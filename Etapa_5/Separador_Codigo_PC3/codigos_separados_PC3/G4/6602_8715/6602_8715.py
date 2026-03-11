alunos = int(input())

i = 0

a = 0
b = 0
c = 0

while i < alunos:
	p = input()
	if p.upper() == "L":
		a += 1
	if p.upper() == "C":
		b += 1
	if p.upper() == "P":
		c += 1
	i += 1
	
print("L=",a)
print("C=",b)
print("P=",c)

