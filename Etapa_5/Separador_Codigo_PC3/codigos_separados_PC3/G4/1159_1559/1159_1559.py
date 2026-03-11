tb = int(input("Digite o numero de tambaquis do viveiro:"))
pc = int(input("Digite o numero de pacus do viveiro:"))
ptb = float(input("Digite a taixa de crescimento anual de tambaquis:"))
ppa = float(input("Dgigite a taixa de crescimento anual de pacus:"))
qm = int(input("digite a quantidade maxima"))
soma = 0
i = 1
while(soma < qm):
	qb = tb *ptb
	tb = tb + qb
	qp = pc * ppa
	pc = pc + qp
	soma = soma + tb + pc
	i = i + 1
print(i)
	
	
