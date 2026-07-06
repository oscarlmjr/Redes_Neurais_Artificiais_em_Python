"""
y = 1 / 1 + e**-x
"""
import numpy as np


entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
pesos0 = [[-0.424, -0.740, -0.961], [0.358, -0.577, -0.469]]
pesos1 = [[-0.017, -0.893, 0.148]]
epocas = 100
somaSinapse = 0

def sigmoid(soma):
	return 1 / (1 + np.exp(-soma))

def soma_sinapse(entrada):
	def interna(peso, indice_entrada):
		somaSinapse = entrada[indice_entrada] * peso
		return somaSinapse

	return interna

for entrada in entradas:
	indice_peso = 0
	variavel = soma_sinapse(entrada)
	somaSinapse1 = 0
	while indice_peso < len(pesos0[0]):
		somaSinapse0 = 0
		indice_pesos = 0
		indice_entrada = 0
		while indice_pesos < len(pesos0):
			camadaEntrada = variavel(pesos0[indice_pesos][indice_peso], 
			indice_entrada)
			somaSinapse0 += camadaEntrada
			indice_entrada += 1	
			indice_pesos += 1
			if indice_pesos == len(pesos0):
				indice_entrada = 0
		indice_peso += 1

		camadaOculta = sigmoid(somaSinapse0) 
		print('camadaOculta', camadaOculta)

		somaSinapse1 += camadaOculta * pesos1[0][indice_peso - 1]
		print('somaSinapse1', somaSinapse1)

	camadaSaida = sigmoid(somaSinapse1)
	print('camadaSaida', camadaSaida)
	print()
