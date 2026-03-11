altura_chico = 1.5
taxa_chico = 0.02

altura_x = float (input("Digite a altura: "))
taxa_x = float (input("Digite a ua taxa de crescimento: "))
count = 0

while (altura_chico > altura_x):
	altura_chico = altura_chico + taxa_chico
	altura_x = altura_x + taxa_x
	count = count + 1
print(count)