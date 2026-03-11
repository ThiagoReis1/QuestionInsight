from numpy import*
v = input("Insira as etnias: ")
vf = v.split(',')
b = 0
pa = 0
pr = 0
a = 0
y = 0
for i in range(size(vf)):
	if vf[i]=="B":
		b = b + 1
	elif vf[i]=="PA":
		pa = pa + 1
	elif vf[i]=="PR":
		pr = pr + 1
	elif vf[i]=="A":
		a = a + 1
	elif vf[i]=="I":
		y = y + 1
print(max(b,pa,pr,a,y))
a = [b,pa,pr,a,y]
print(array(a))
