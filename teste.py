#Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. 
#Esse programa deve calcular e mostrar:  
#a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.  
#b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%. 
#Observe que as quantidades calculadas devem ser um número inteiro, portanto, 
#o resultado da quantidade de convites deve ser arredondada para cima, usando a função matemática apropriada em Python. 

import math
custo = float (input('Digite o custo do espetáculo: R$ '))
preco = float (input('Digite o preço do convite: R$ '))


convite_custo = math.ceil(custo/preco)
lucro = custo * 0.23
convite_lucro = math.ceil((custo + lucro) / preco)


print(f"Para alcançar o custo do espetáculo, é necessário vender {convite_custo} convites.")
print(f"Para ter um lucro de 23%, é necessário vender {convite_lucro} convites.")