import random
import string


print('Bem-vindo(a) ao Gerador de senha segura!')
tamanho = int(input('Defina o tamanho da sua senha (minimo = 10): '))

def gerador_senha(tamanho):
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    senha = ''
    for i in range(tamanho):
        senha += random.choice(caracteres)
    
    return senha

print(f'A senha segura gerada eh: {gerador_senha(tamanho)}' if tamanho >= 10 else 'Senha muito pequena')
