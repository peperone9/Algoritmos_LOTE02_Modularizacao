#declarar
tipo_invest: int
valor: float

#inicio
tipo_invest = int(input("Tipo de investimento([1] poupanca [2] renda fixa):"))
valor = float(input("Valor a ser investido: R$"))

if(tipo_invest > 0 and tipo_invest < 3 and valor > 0 ):
	if(tipo_invest == 1):
		valor *= 1.03
	else:
		valor *= 1.05
	print("Valor Corrigido: R$", valor)
else:
	print("Tipo de investimento ou valor inválido !!")
