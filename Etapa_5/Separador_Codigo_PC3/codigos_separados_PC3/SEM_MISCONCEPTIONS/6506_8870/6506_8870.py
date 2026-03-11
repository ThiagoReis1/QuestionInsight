# faça seu código aqui!

PRECO_REFEICAO = 40.0
DESCONTO = 0.05

pratos = int(input("Pratos consumidos: "))
sobremesa = input("Deseja sobremesa? (s para sim, n para nao): ").lower()

total = pratos*PRECO_REFEICAO

if sobremesa == 's':
    total = total*(1-DESCONTO)
	
print(round(total, 2))