volume_agua= float(input("qual o volume de agua consumido?"))

valor_mes= (volume_agua * 0.37) + 15

porc= valor_mes *35 /100

custo_total= valor_mes + porc

print(round(custo_total, 2))