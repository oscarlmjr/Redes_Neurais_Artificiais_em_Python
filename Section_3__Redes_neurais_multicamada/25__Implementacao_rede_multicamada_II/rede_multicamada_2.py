"""
y = 1 / 1 + e**-x
"""
import numpy as np


entradas = [[0, 0], [0, 1], [1, 0], [1, 1]]
pesos0 = [[-0.424, -0.740, -0.961], [0.358, -0.577, -0.469]]
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
	while indice_peso < len(pesos0[0]):
		soma = 0
		indice_pesos = 0
		indice_entrada = 0
		while indice_pesos < len(pesos0):
			print('ind_pesos', indice_pesos, 'ind_peso', indice_peso, 
			'ind_entrada', indice_entrada)
			# print(variavel(pesos0[indice_pesos][indice_peso], indice_entrada))
			funcao_sigmoide = variavel(pesos0[indice_pesos][indice_peso], indice_entrada)
			soma += funcao_sigmoide
			print(funcao_sigmoide)
			indice_entrada += 1	
			indice_pesos += 1
			if indice_pesos == len(pesos0):
				# indice_pesos = 0
				indice_entrada = 0
		indice_peso += 1	

		print(sigmoid(soma))
	print()
