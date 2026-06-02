"""
y = 1 / 1 + e**-x
d = y * (1 - Y)
erro = respostaCorreta - respostaCalculada
DeltaSaida = Erro * DerivadaSigmoide
DeltaEscondida = DerivadaSigmoide * peso * DeltaSaida
peso(n + 1) = (peso(n) * momento) + (entrada * delta * taxa de aprendizagem)
N = quantidade de registros, ex.: (0,0), (0,1), (1,0), (1,1)
Mean Square Error: MSE = 1/N Somatorio i=1, N (fi - yi)**2
Root Mean Square Error: RMSE =  1/N Somatorio i=1, N (fi - yi)**2)**1/2
"""