from math import*
x = int(input("Digite a quantidade inicial de tambaquis: "))
y = float(input("Digite a taxa: "))
z = int(input("Digite os tambaquis tirados anualmente: "))
anos = 3
n = 1
while(n<=x):
	anos = anos + 1
	n = n + 1
	x = x - z
print(anos)