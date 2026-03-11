dado = int(input("Digite uma das faces: "))
l = 0
total = 0

while (dado != -1):
		dado = dado + l 
		total = total + (l * 0.06)
print(total)