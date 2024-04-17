import math

def eh_divisivel_por_3_e_5(numero):
  return math.gcd(numero, 3) == 1 and math.gcd(numero, 5) == 1
numero = int(input("Digite um número inteiro: "))
if eh_divisivel_por_3_e_5(numero):
  print("O número é divisível por 3 e 5.")
else:
  print("O número não é divisível por 3 e 5.")

