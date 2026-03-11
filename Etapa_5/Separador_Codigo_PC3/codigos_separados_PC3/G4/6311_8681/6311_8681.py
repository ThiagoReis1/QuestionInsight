from numpy import * 
a = input("Insira a secao do produto: ").upper()
i = 0 #contador
t = 0 #valor total da compra
x = 0 
y = 0 
z = 0 

while i < len(a):
	if a[i]=="C":
		t = t + 10.50
		x = x + 1
	if a[i]=="E":
		t = t + 8.75
		y = y + 1
	if a[i]=="P":
		t = t + 17.90
		z = z + 1
	i = i + 1
print(round(t,2), x, y, z)