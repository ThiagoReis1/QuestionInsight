N = (input("Tipo de ataque:"))
d1 = int(input("Digite a face:"))
d2 = int(input("Digite a face:"))
d3 = int(input("Digite a face:"))
d4 = int(input("Digite a face:"))
atq1 =  (d1+6)+(d2+6)+(d3+6)+(d4+6)
atq2 = (d1 + d2 + d3)*d4
if(N == "cauda"):
	print(atq2)
if(N == "espada"):
	print(atq1)

