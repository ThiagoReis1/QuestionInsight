peso = float(input("Digite o valor do peso do saco de racoes em gramas: "))
qd = float(input("Digite a quantidade diaria de racao em gramas: "))

saldo = peso - (qd * 5) 

print(round(saldo,3))