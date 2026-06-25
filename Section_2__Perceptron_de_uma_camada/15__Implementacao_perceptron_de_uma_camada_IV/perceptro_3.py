# erro = respostaCorreta - respostaCalculada
# novoPeso = peso(n + 1) = peso(n) + (taxaAprendizagem * entrada * erro)

entradas = [[0,0],[0,1], [1,0], [1,1]]
pesos = [0.0, 0.0]
saidas = [0, 0, 0, 1]
taxaAprendizagem = 0.1

def treinar(entradas, pesos):
    for indice, entrada in enumerate(entradas):
        respostaCalculada = 0
        for c, e in enumerate(entrada):
            print('c:', c, ', e:', e)
            respostaCalculada += e * pesos[c]
            respostaCorreta = saidas[indice]
       
        print('respostaCalculada', respostaCalculada)
        print('respostaCorreta', respostaCorreta)
       
        if respostaCalculada < 1:
            respostaCalculada = 0
        erro = abs(respostaCorreta - respostaCalculada)
        if erro >= 1:
            print('\nERRO')
            pesoNovo = []
            for c, e in enumerate(entrada):
                respostaCalculada += e * pesos[c]
                respostaCorreta = saidas[indice]
                pesoNovo.append(pesos[c] + (taxaAprendizagem * e * erro))
            pesos = pesoNovo
            print('pesos', pesos)
       
            return treinar(entradas, pesos)
   
    return stepFunction(respostaCalculada)
   
def stepFunction(respostaCalculada):
    if respostaCalculada >= 1:
        return 1
    return 0


print(treinar(entradas, pesos))
print('Rede neural treinada')

# erro = respostaCorreta - respostaCalculada
# novoPeso = peso(n + 1) = peso(n) + (taxaAprendizagem * entrada * erro)