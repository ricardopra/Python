def main():
    valor = float(input())
    dias = int(input())
    print(valorPagamento(valor,dias))

def valorPagamento(valor, dias):
    if dias > 0:
        multa = valor * 0.03
        juros = valor * (dias * 0.001)
        return valor + multa + juros
    else:
        return valor

main()  