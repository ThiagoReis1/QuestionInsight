string = input("digite um nome: ").upper()
n = 0
count_p = 0
while n < count_p(string):
	if string[n] == "n":
		print(n)
		count_p = count_p + 1 
	n = n + 1
if count_p == 0:
	print("nome invalido")