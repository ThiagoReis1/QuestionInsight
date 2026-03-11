total = 80000
qpi = int(input(""))# quant. inicial de pergaminhos
qvi = int(input(""))# quant. de varinhas magicas
percp = float(input(""))#perc. de pergaminhos
percv = float(input("")) #percentual de varinhas
t = 0

while((qpi+qvi)<total):
	qpi = qpi+qpi*(percp/100)
	qvi = qvi+qvi*(percv/100)
	t= t+1
print(t)
	