#EXERCÍCIO 1 - Escreva um programa em Python que permita ao usuário digitar dois números inteiros e 
#exibir o resultado para cada uma das seguintes operações, nesta ordem: soma, subtração, multiplicação, 
#divisão, divisão truncada, resto e exponenciação.

print ('digite 2 numeros: ')
var1 = int(input())
var2 = int(input())

soma = var1 + var2
sub = var1 - var2
multi = var1 * var2
div = var1 / var2
divt = var1 // var2
rest = var1 % var2
exp = var1 ** var2


print ('soma dos 2 números: ', soma)
print ('subtração dos 2 números: ', sub)
print ('multiplicação dos 2 números: ', multi)
print ('divisão dos 2 números: ', div)
print ('divisão truncada dos 2 números: ', divt)
print ('resto dos 2 números: ', rest)
print ('exponenciação dos 2 números: ', exp)
