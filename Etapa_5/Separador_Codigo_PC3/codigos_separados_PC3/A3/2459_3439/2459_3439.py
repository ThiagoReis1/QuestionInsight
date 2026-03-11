
peso = int(input("qual o peso:"))
dis = int(input("qual a dis:"))
codigo = int(input("qual o codigo:"))
custo1 = 25,0
custo2 = 0,10
icms = 72,5 
total = (peso*custo1 + dis*custo2)*(1,0 + icms // 100)
print(round(total, 2))
