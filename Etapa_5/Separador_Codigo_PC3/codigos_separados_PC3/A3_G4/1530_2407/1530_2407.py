p = int(input("Quantidade inicial de pergaminhos: "))
v = int(input("Quantidade inicial de varinhas: "))
pp = float(input("percentual de crescimento de pergaminhos: "))
pv = float(input("percentual de crescimento de varinhas: "))

limite = 80000

anos = 0 

while (p+v <= 80000):
	p = p + (p/100)*pp
	v = v + (v/100)*pv
	anos = anos+1

print(anos)	