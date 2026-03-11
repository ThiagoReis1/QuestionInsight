qp= int(input("pergaminhos: "))
qv= int(input("quantidade de varinhas: "))
pap= int(input("percentual de pergaminhos: "))
pav= int(input("percentual de varinhas: "))
soma = 0

anos = 0

while (soma <= 80000):
	qp = qp + (pap/100)
	qv = qv + (pav/100)
	soma = soma + (qp+qv)
	anos = anos+1

print(anos)



    