import secrets

def gerador_senha():
    # Gera uma senha aleatória de 32 bits
    return secrets.token_hex(4)

# Testa o gerador de senha
print(gerador_senha())
