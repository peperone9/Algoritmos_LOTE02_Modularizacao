#25 -Receba a hora de início e de final de um jogo (HH,MM), calcular o 
#tempo do jogo em horas e minutos, sabendo que o tempo máximo é 
#menor que 24 horas e pode começar num dia e terminar noutro

#declarar
h_inicio: int
h_fim: int
h_total: int

min_inicio: int
min_fim: int
min_total: int

#inicio

#pega hora e minuto iniciais
def tempo_inicial():
	global h_inicio
	global min_inicio
	h_inicio = int(input())
	min_inicio = int(input())

#pega hora e minuto finais
def tempo_final():
	global h_fim
	global min_fim

	h_fim = int(input())
	min_fim = int(input())

#calcula hora total
def hora_total():
	global h_total

	if(h_inicio < h_fim):
		h_total = h_fim - h_inicio
	else:
		h_total =  (24 - h_inicio) + h_fim

#calcula minuto total
def min_total():
	global min_total
	global h_total

	if(min_inicio < min_fim):
		min_total = min_fim - min_inicio
	elif(min_inicio > min_fim):
		min_total = (60 - min_inicio) + min_fim

		h_total -= 1
	else:
		min_total = 0

def tempo_jogo():
	#valida se o jogo passou de 1 dia
	if(h_total >= 24):
		print("O jogo não pode durar mais que um dia")
	else:
		print("O jogo durou", h_total,"horas e", min_total,"minutos")
	#fim

def main():
	tempo_inicial()
	tempo_final()
	hora_total()
	min_total()
	tempo_jogo()
main()
