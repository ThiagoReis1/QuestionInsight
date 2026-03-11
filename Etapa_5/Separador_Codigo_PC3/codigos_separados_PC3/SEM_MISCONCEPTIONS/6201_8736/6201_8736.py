altura_joe = 1.77
taxa_joe = 0.02
altura_adenison = float(input("Altura do rapaz : "))
taxa_ryan = float(input("Taxa de crescimento : "))
acm = 0

while (altura_joe > altura_adenison):
	acm = acm + 1
	altura_joe = altura_joe + taxa_joe 
	altura_adenison = altura_adenison + taxa_ryan 
print(acm)