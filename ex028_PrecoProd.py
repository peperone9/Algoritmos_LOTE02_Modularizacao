
def calcula_preco(preco_atual: float, media: float):
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

def ler_entradas():
	#declarar
	preco_atual: float
	novo_preco: float
	media: float

	preco_atual = float(input("Preco atual do produto: ")) #do produto
	media = float(input("Media de vendas: ")) #media de vendas

	calcula_preco(preco_atual, media)

def main():
	ler_entradas()
main()
