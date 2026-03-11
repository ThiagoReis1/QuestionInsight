#Lamen do Ichiraku

ram = float(input("Quantos ramens? "))

men = float(input("Quantos menmas? "))

bol = float(input("Quantos bolinhos de arroz? "))

oni = float(input("Quantos onigis? "))

total = ram*7.0 + men*6.0 + bol*3.0 + oni*5.0

if(total <= 42):
	print(round(total - 3,2), "ryous")
else:
	print(round(total - total*10/100,2), "ryous")