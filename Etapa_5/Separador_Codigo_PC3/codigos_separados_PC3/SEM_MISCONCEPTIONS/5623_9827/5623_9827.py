opcao = input()
qtd = int(input())
capp = int(input())

if opcao.upper() == 'B':
	print(round((5.0 * qtd)+ (7.50 * capp),1))
if opcao.upper() == 'S':
	print(round((4.0 * qtd)+ (7.5 * capp),1))