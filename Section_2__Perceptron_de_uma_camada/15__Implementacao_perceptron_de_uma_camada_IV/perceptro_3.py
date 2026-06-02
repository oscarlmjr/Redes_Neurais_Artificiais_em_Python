# erro = respostaCorreta - respostaCalculada
# novoPeso = peso(n + 1) = peso(n) + (taxaAprendizagem * entrada * erro)

import numpy as np


entradas = np.array([[0,0], [1,0], [0,1], [1,1]])
saidas = np.array([0,1,1,0])
pesos = np.array([[0.0, 0.0]])
taxaAprendizagem = 0.1



