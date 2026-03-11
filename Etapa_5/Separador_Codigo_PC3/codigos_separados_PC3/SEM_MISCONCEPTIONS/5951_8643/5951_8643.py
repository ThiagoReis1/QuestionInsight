tous = input("d ou s:").upper()
tapousal = int(input("quantas:"))
qtda = int(input("quantidade:"))

tapio = tapousal*4.50
salg = tapousal*5.00
acai = qtda*12

if(tous == "T"):
	print(round(tapio + acai, 2 ))
else:
	print(round(salg + acai, 2))