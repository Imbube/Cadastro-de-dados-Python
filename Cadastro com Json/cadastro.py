import json
import os

arquivo_usuarios = 'usuarios.json'

# Carrega os dados se o arquivo já existir
if os.path.exists(arquivo_usuarios):
    with open(arquivo_usuarios, 'r') as f:
        usuarios = json.load(f)
else:
    usuarios = {}  # Começa vazio se o arquivo não existe

check_user = input('Olá usuário, você já é cadastrado? Digite sim ou nao: ').strip().lower()

if check_user == 'nao':
    print('Seja bem-vindo ao sistema! Vamos fazer seu cadastro.')
    user = input('Digite seu nome de usuário: ')
    name = input('Digite seu nome completo: ')
    age = int(input('Digite sua idade: '))
    
    usuarios[user] = {'nome': name, 'idade': age}

    # Salva os dados no arquivo
    with open(arquivo_usuarios, 'w') as f:
        json.dump(usuarios, f)

    print('Cadastro realizado com sucesso!')
    print(f'Nome: {name}\nIdade: {age}')

elif check_user == 'sim':
    print('Seja bem-vindo(a) de volta! Faça seu login.')
    user_login = input('Digite seu nome de usuário: ')
    
    if user_login in usuarios:
        print('Seus dados são:')
        print(f"Nome: {usuarios[user_login]['nome']}\nIdade: {usuarios[user_login]['idade']}")
    else:
        print('Usuário não encontrado.')

else:
    print('Opção inválida.')

print('Operação encerrada.')
