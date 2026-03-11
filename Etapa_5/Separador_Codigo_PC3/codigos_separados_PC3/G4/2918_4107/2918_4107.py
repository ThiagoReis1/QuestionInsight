var1 = float(input("Preco do ingresso:"))
var2 = float(input("Quantidade de ingressos:"))

var3= var1*var2 

total= var3-(var3*(20/100))

print(round(total, 2))
