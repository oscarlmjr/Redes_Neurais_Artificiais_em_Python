entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]
somatorio = 0


def soma(entrada, peso):
    print(entrada, peso)
    somatorio =+ entrada * peso
    print(somatorio)


for entrada in entradas:
    for peso in pesos:
        soma(entrada, peso)
        break

def step(somatorio):
    if somatorio >= 1:
        return 1 
    return 0

step_function = step(somatorio)
print(step_function)
