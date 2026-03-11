choice= input("Tapioca ou Salgado? ")
qntd = float(input("Quantos? "))
acais = float(input("QUantos acais? "))
total1 = acais * 13 
if choice == "S": 
	total = total1 + (qntd * 5)
else: 
	total = total1 + (qntd * 3.5)
print(total)