alturaalice = 1.6
taxaalice = 0.02
altura = float(input("altura: "))
taxa = float(input("taxa: "))
cont = 0
while altura < alturaalice:
	if taxa < 1.6:
		altura = altura + taxa
		cont = cont + 1
print(altura)
		