#EXERCÍCIO 3 – Faça um programa em Python que resolva o seguinte problema: 
#Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 
#- o primeiro ganhador receberá 46% do prêmio; 
#- o segundo ganhador receberá 32% do prêmio; 
#- o terceiro ganhador receberá o restante do prêmio. 
#Calcule e mostre o valor do prêmio de cada ganhador, nesta ordem: primeiro colocado, segundo colocado e terceiro colocado.
#Observe que este programa não tem valor de entrada feita pelo usuário. 


varPremio = float (780000.00)

varPrimeiro = float (varPremio * 0.46)
varSegundo = float (varPremio * 0.32)
varTerceiro = float (varPremio - varPrimeiro - varSegundo)

print("Primeiro colocado:", f"R${varPrimeiro:.2f}")
print("Segundo colocado:", f"R${varSegundo:.2f}")
print("Terceiro colocado:", f"R${varTerceiro:.2f}")