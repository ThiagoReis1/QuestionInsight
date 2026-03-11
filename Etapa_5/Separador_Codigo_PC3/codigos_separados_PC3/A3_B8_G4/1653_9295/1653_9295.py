from numpy import*
v = input("").upper()
v = v.split(',')
i = 0
a = 0
b = 0
cl = 0
co = 0
uy = 0

while i <= size(v):
	if v[i] == "BR":
		b += 1
	elif v[i] == "AR":
		a += 1
	elif v[i] == "CL":
		cl += 1
	elif v[i] == "CO":
		co += 1
	elif v[i] == "UY":
		uy += 1

z = array(eval(vet[ar,br,cl,co,uy]))
y = max(z)
print(y)
print(z)


