altura_bia = 1.69
taxa_bia = 0.01

f = float(input("abra: "))
t = float(input("abra: "))

a = 0

while(f <= altura_bia):
	altura_bia += taxa_bia
	f += t
	a += 1
print(a)
	