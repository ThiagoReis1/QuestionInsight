valor=float(input("Qual o preco: "))
quantidade=int(input("Qual a quantidade: "))
desconto=20
promocao= valor-(valor*(desconto/100))
total= promocao * quantidade
print(round(total, 2))