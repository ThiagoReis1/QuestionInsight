b = int(input("digite:"))
t = int(input("digite:"))

d = b*2
cont = 0
while b < d:
	b = b+(b*t)/100
	cont = cont+1
if b >= d:
	print(cont)
