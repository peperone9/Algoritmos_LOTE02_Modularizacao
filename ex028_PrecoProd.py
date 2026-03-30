#declarar
preco_atual: float
novo_preco: float
media: float

#inicio
preco_atual = float(input()) #do produto
media = float(input()) #media de vendas

if((media < 500) and (preco_atual < 30.00)):
	novo_preco = preco_atual * 1.10
elif(
	(media >= 500 and media < 1000) and
	(preco_atual >= 30.00 and preco_atual < 80.00)
):
	novo_preco  = preco_atual * 1.15
elif((media >= 1000) and (preco_atual >= 80.00)):
	novo_preco = preco_atual * 0.95
else:
	novo_preco = preco_atual

print("novo preco: R$", novo_preco)
#fim

