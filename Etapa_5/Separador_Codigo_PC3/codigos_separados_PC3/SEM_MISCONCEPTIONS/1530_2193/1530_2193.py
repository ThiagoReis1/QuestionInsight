perga1 = int(input("Quantidade de pergaminhos:"))
var1 = int(input("Quantidade de varinhas:"))

perga2 = float(input("Percentual pergaminhos:"))
var2 = float(input("Percentual varinhas:"))

anos = 0

while (perga1 + var1 < 80000):
	perga1 = perga1 + (perga1 * (perga2/100))
	var1 = var1 + (var1 * (var2/100))
	anos = anos + 1
print(anos)

