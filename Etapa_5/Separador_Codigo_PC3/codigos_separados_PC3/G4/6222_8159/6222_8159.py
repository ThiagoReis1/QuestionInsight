x=int(input("DIgite um numero x: "))
y=int(input("Digite um numero y: "))
s=0
while x <= y:
	if x % 2 == 0 :
		s += x
	x += 1
print(s)