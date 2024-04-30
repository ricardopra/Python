# Faça um programa modularizado em Python com as seguintes funções: 
# a) atualiza_preco(valor): a função deve receber como parâmetro o valor de um produto, calcular e retornar este valor com aumento de 10%
# b) taxa(valor): a função calcula e retorna o valor da taxa de 2.5% sobre o valor do produto atualizado 
# (após a chamada da função atualiza_preco). 
# c) main(): terá o programa principal que deve, nesta ordem, fazer a entrada via teclado (digitada pelo usuário) do valor do produto, 
# depois chamar as funções atualiza_preco e taxa e apresentar os valores calculados do valor atualizado 
# com duas casas decimais e do valor da taxa também com duas casas decimais. 
# Ao final, chame a função main() para que o programa seja executado.

def atualiza_preco(valor):
    valor_atualizado = valor * 1.10  
    return valor_atualizado

def taxa(valor):
    valor_taxa = valor * 0.025  
    return valor_taxa

def main():
    valor = float(input("Digite o valor do produto: "))
    valor_atualizado = atualiza_preco(valor)
    valor_taxa = taxa(valor_atualizado)

    print(f"Valor atualizado: {valor_atualizado:.2f}")
    print(f"Valor da taxa: {valor_taxa:.2f}")

main()


