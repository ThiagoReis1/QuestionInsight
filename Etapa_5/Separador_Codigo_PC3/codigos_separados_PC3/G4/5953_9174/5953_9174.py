x = 6.00
y = 13.50
z = 3.00

lanche = input("Lanche ou Prato: ")
qntd = int(input("quantidade lanche ou prato: "))
qntd_2 = int(input("quantidade refri: "))

if lanche == "L":
	c = qntd * x + qntd_2 * z
	print(c)

else: 
	d = qntd * y + qntd_2 * z
	print(d)