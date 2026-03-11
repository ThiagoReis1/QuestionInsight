# faça seu código aqui!
n = int(input())
t = 0
a = 0
v = 0
cont = 0
while (cont < n):
	q = input().upper()
	if (q == "A"):
		t = t + 1
	elif (q == "B"):
		a = a +1
	elif (q == "C"):
		v = v + 1
	cont= cont +1
	
print("A=",t)	
print("B=",a)
print("C=",v)
#print(cont)
