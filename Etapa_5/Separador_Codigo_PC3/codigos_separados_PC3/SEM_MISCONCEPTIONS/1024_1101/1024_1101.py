lado_a = float(input("o lado a: "))
lado_b = float(input("o lado b: "))
lado_c = float(input("o lado c: "))
preco_por_metro = float(input("qual o preço por metro? "))
servico = (lado_a + lado_b + lado_c) * preco_por_metro

print(round(servico, 2))