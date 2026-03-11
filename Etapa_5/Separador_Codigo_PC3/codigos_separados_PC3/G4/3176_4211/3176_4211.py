from numpy import*
v = input("Digite uma palavra: ").split(',')
c = 0
vo = 0
for i in range(size(v)):
	if(v[i] != 'a' or v[i] != 'e' or v[i] != 'i' or v[i] != 'o' or v[i] != 'u'):
		vo = vo + 1		
	else:
		c = c + 1
print(vo)
print(c)