altura_max = 1.75
taxa_max = 0.01
num1 = float(input("numero 1:"))
num2 = float(input("numero 2 :"))
anos = 0
###############################3
while num1 < altura_max:
	altura_max += 0.01
	num1 += num2
	anos += 1
print(anos)