# soma = somatorio(i=1 -> n) xi * wi
# entradas = [1, 7 , 5]
entradas = [-1, 7 , 5]
pesos = [0.8, 0.1 , 0]


def soma(contador, somatorio):

	multiplica = pesos[contador] * entradas[contador]
	somatorio += multiplica	
	# print(f'{pesos[contador]} * {entradas[contador]} = {multiplica}')
	# print(f'{somatorio=}\n')
	contador += 1
	if contador == len(entradas):
		return somatorio

	return soma(contador, somatorio)

def stepFunction(funcao_somatoria):   # Função Degrau
	if funcao_somatoria >= 1:
		return 1
	return 0


funcao_somatoria = soma(0, 0)
print(funcao_somatoria, '\n')

resultado_step_function = stepFunction(funcao_somatoria)
print(resultado_step_function, '\n')
