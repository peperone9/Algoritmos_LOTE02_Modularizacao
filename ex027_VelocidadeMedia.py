#27. Receba o número de voltas, a extensão do circuito (em metros)
#e o tempo de duração(minutos). Calcule e mostre a velocidade
# média em km/h.
#declarar
voltas: int
tam_circ: float
duracao: int

def ler_entradas():
	global voltas 
	global tam_circ
	global duracao

	voltas = int(input("numero de voltas no circuito: "))
	tam_circ = float(input("tamanho do circuito(metros):"))
	duracao = int(input("duracao do circuito(minutos):")) #em minutos
	valida_entrada()

def valida_entrada():
	if(voltas <= 0 or duracao <= 0 or tam_circ <= 0):
		print("Os valores não podem ser inexistentes!!\n")
		ler_entradas()

def calcula_velocidade(voltas, tam_circ, duracao):
	valida_entrada()
	velocidade = (voltas * tam_circ) / duracao
	return velocidade * 0.06
	
#fim

def main():
	global voltas
	global tam_circ
	global duracao 
	velocidade: float 

	ler_entradas()
	
	velocidade = calcula_velocidade(voltas, tam_circ, duracao)

	print("velocidade:", velocidade,"km/h")
main()
