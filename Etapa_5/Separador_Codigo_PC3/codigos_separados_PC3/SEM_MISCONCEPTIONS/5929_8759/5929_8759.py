agua= float(input("bote a quantidade do volume de agua consumida nesse mes "))

valor= (agua * 0.37) + 15.00 
valor= valor +(valor * (35/100))

print(round(valor, 2))