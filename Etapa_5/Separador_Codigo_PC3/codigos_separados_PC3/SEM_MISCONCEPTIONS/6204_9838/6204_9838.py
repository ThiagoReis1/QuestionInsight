ac = float(input("Altura coelho: "))
tc = float(input("Taxa de crescimento: "))

altura_macaco=1.86
taxa_macaco = 0.01

ano = 1


while (altura_macaco > ac):
	altura_macaco = altura_macaco + (altura_macaco*taxa_macaco)
	ac = ac + ac*(tc)
	ano = ano + 1
	
print(ano)