qtde = int(input())
cont = 0
soma=0
while cont<qtde:
    media = float(input())
    if media>=6.0:
        print('PARABÉNS VOCÊ ESTÁ APROVADO')
    soma+=media
    cont+=1
if qtde!=0:
    print(soma/qtde)
else:
    print('NÃO HOUVE PROCESSAMENTO')

