valorkg= 25.00
valorkm=0.10

peso= float(input("digite um valor"))
d= float(input("digite um valor"))

preco=(valorkg*peso)+(valorkm*d)

imposto_icms= preco*(12/100)

valortransporte= preco+imposto_icms

print(round(valortransporte,2))

