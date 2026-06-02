# soma = somatorio(i=1 -> n) xi * wi
import numpy as np


entradas = np.array([0, 1])
pesos = np.array([0.5, 0.5])

def soma(entradas, pesos):   # entradas.dot(pesos)

	return entradas.dot(pesos)

def stepFunction(funcao_somatoria):   # Função Degrau
	if funcao_somatoria >= 1:
		return 1
	return 0


funcao_somatoria = soma(entradas, pesos)
print(funcao_somatoria, '\n')

resultado_step_function = stepFunction(funcao_somatoria)
print(resultado_step_function, '\n')
