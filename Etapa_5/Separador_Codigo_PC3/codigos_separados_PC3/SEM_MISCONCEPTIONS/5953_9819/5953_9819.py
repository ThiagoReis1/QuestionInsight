opcao = input() 
P = int(input())
refri = int(input()) 

if opcao == "L":
	v = P * 6 + refri*3
	print(round(v ,2))
else:
	v = P * 13.50 + refri*3
	print(round(v ,2))