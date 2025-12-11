import bcrypt
import time

# Caso não tiver o bcrypt no pacote instalado do Python em sua máquina, use --> pip install bcrypt <-- no terminal

# Caso deseje inserir uma palavra-chave fixa, use o prefixo 'b' para criar uma string de byte
#password = b"palavra-chave"

# Para receber uma entrada de um usuário,utilize o método .encode("utf-8")
# O bcrypt só trabalha com dados em formato de bytes
password = input("Digite a palavra-chave a ser cifrada: ").encode("utf-8")

# bcrypt.gensalt() gera um "salt" aleatório, um valor extra que torna o hash único (128 bits)
# hashpw() aplica o algoritmo bcrypt para gerar o hash da senha
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("\nO resultado é: ")
print(hashed)

print("\nVerificando a senha...")
password_test = input("\nDigite novamente a senha para verificar: ").encode("utf-8")

# DEMONSTRAÇÃO:
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Percebe-se que o hash é diferente
print("\nO resultado é: ")
print(hashed)

"""
--- COMPARAÇÃO DE SENHA ---

Mesmo que a senha seja igual, o hash gerado não será, pois:

- bcrypt.gensalt() gera um valor único a cada vez
- o valor é incorporado ao hash. Com isso, torna-se único
- mesma senhas, hashes diferentes

checkpw() consegue distinguir
"""
if bcrypt.checkpw(password_test, hashed):
    print("\nSenha correta!")
else:
    print("\nSenha incorreta!")