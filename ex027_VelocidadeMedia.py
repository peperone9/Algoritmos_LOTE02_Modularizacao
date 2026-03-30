#27. Receba o número de voltas, a extensão do circuito (em metros)
#e o tempo de duração(minutos). Calcule e mostre a velocidade
# média em km/h.

#declarar
voltas: int
duracao: int

tam_circ: float

#inicio
voltas = int(input("numero de voltas no circuito: "))
tam_circ = float(input("tamanho do circuito(metros):"))
duracao = int(input("duracao do circuito(minutos):")) #em minutos

velocidade: float

if(voltas <= 0 or duracao <= 0 or tam_circ <= 0):
	velocidade = 0
else:
	velocidade = (voltas * tam_circ) / duracao
	velocidade *= 0.06
print("velocidade:", velocidade,"km/h")
#fim
