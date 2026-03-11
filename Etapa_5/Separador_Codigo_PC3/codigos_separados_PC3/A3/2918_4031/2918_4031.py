valor=float(input("valor do ingresso: "))
quant=float(input("quantidade de ingresso: "))
var=20/100
desconto=var
promocao=valor-(valor*(desconto/100))
print(round(promocao, 2))
