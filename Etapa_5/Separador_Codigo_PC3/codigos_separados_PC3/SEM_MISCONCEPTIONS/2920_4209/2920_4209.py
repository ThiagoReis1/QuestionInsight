grama=float(input())
bebidas=int(input())
sobremesa=int(input())
conv=grama/1000
fg=conv*26.90
fb=bebidas*3.50
fs=sobremesa*3.00
final=(fg+fb+fs)
print(round(final, 2))
