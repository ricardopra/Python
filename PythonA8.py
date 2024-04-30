# Faça um programa modularizados em Python, para resolver um problema usando listas. 
# O programa deve ter as seguintes funções:
# - entrada_carro(): faz a entrada do modelo de 4 carros via teclado (o usuário irá digitar o modelo de 4 carros),
# - entrada_consumo(): faz a entrada de um número inteiro que é o consumo (em litros) de cada modelo de carro por quilometro (o usuário digita o consumo correspondente a cada carro),
# - economico(): retorna o modelo do carro mais econômico. Observe que o modelo do carro e seu consumo estará na mesma posição na lista, porém em vetores diferentes (carro e consumo).
# A entrada de dados deve ser feita da seguinte forma:
# - O usuário irá digitar o modelo de cada um dos 4 carros, linha por linha em seguida
# - O usuário irá digitar o consumo de cada um dos 4 carros, linha por linha.
# O programa irá apresentar na tela o modelo do carro que tiver o menor valor de consumo.
# def main():
#     entrada_carro()
#     entrada_consumo()
#     print(economico())
# main()
# Entrada
# - O usuário irá digitar o modelo de cada um dos 4 carros, linha por linha em seguida
# - O usuário irá digitar o consumo de cada um dos 4 carros, linha por linha.
# Saída
#  o modelo do carro que tiver o menor valor de consumo

def entrada_carro():
    carros = []
    for i in range(4):
        carro = input()
        carros.append(carro)
    return carros

def entrada_consumo():
    consumos = []
    for i in range(4):
        consumo = int(input())
        consumos.append(consumo)
    return consumos

def economico(carros, consumos):
    index_economico = consumos.index(min(consumos))
    return carros[index_economico]

def main():
    carros = entrada_carro()
    consumos = entrada_consumo()
    print(economico(carros, consumos))

main()

