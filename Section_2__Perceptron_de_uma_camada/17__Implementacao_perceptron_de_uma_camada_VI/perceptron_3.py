# erro = respostaCorreta - respostaCalculada
# novoPeso = peso(n + 1) = peso(n) + (taxaAprendizagem * entrada * erro)
import numpy as np


entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
pesos = np.array([0.0, 0.0])
# saidas = np.array([0, 0, 0, 1])
saidas = np.array([0, 1, 1, 1])
taxaAprendizagem = 0.1

def treinar(entradas, pesos):
    erroTotal = 0
    for indice, entrada in enumerate(entradas):
        respostaCalculada = 0
        respostaCalculada = entrada.dot(pesos)
        respostaCorreta = saidas[indice]
       
        if respostaCalculada < 1:
            respostaCalculada = 0
        else:
            respostaCalculada = 1

        erro = abs(respostaCorreta - respostaCalculada)

        if erro >= 1:
            erroTotal += erro
            pesoNovo = []
            for c, e in enumerate(entrada):
                pesoNovo.append(pesos[c] + (taxaAprendizagem * e * erro))
            print('Peso atualizado: ', *pesoNovo)

    if erroTotal >= 1:
        pesos = pesoNovo
        print('Total de erros: ', erroTotal)

        return treinar(entradas, pesos)

    print('Total de erros: ', erroTotal)
          
    return stepFunction(respostaCalculada)
   
def stepFunction(respostaCalculada):
    if respostaCalculada >= 1:
        return 1
    return 0


print(treinar(np.asarray(entradas), pesos))
print('Rede neural treinada')

# erro = respostaCorreta - respostaCalculada
# novoPeso = peso(n + 1) = peso(n) + (taxaAprendizagem * entrada * erro)