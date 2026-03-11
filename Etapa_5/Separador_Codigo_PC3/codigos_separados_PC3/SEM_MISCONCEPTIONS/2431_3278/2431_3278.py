passagem_cliente = float(input("valor da passagem do cliente"))
passagem_acomp= float(input("valor passagem do acompa"))
desconto= passagem_acomp - (passagem_acomp * (35 / 100))
total= passagem_cliente + desconto
print(round(passagem_cliente,2))
print(round(desconto,2))
print(total)