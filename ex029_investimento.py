#declarar
tipo_invest: int =  0
valor: float = 0


def valida_entrada(tipo, v):
	if(tipo <= 0 or tipo >= 3 or v < 0 ):
		print("Tipo de investimento ou valor inválido !!\n")
		ler_dados(tipo, v)

def ler_dados(tipo: int, v: float):
	global tipo_invest
	global valor 

	tipo = int(input("Tipo de investimento([1] poupanca [2] renda fixa):"))
	v = float(input("Valor a ser investido: R$"))
	valida_entrada(tipo, v)
	tipo_invest = tipo 
	valor = v

def novo_valor(tipo, v):
	global tipo_invest
	global valor
	valida_entrada(tipo_invest, valor)

	if(tipo_invest == 1):
		valor *= 1.03
	else:
		valor *= 1.05
	print("Valor Corrigido: R$", valor)

def main():
	ler_dados(tipo_invest, valor)
	novo_valor(tipo_invest, valor)
main()