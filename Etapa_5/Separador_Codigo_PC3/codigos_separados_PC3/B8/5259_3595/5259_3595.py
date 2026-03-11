mensalidade = float(input())
crianca = int(input())

if crianca==1:
	valorMensal = mensalidade - mensalidade*0.1
elif crianca == 2:
	valorMensal = crianca*(mensalidade - mensalidade*0.3)
elif crianca >= 3:
	valorMensal = crianca*(mensalidade -  mensalidade*0.4)
	
print(round(valorMensal,2))