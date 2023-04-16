# SISTEMA DE CADASTRO
# CADASTRAR PESSOAS
# GUARDAR INFORMAÇOES
# BUSCAR INFORMAÇOES
# ALTERAR INFORMAÇOES
from pathlib import Path
import sqlite3
from secrets import SystemRandom as sr
import string
# pegando local da pasta
AB = Path(__file__).parent
Namedb = 'dados.db'
CAMINHOCPT = AB / Namedb
#primeira conecção com db
conn = sqlite3.connect(CAMINHOCPT)
cursor = conn.cursor()                
TABELA = 'clients'

def criarTab():
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {TABELA}'
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT,'
        'nome TEXT,'
        'idade REAL,'
        'numero REAL,'
        'sexo TEXT,'
        'senha TEXT'
        ')'
    )
    conn.commit()
criarTab()

def adicionarTab(nome:str, idade:int, numero:int, sexo:str, senha:str):
    cursor.execute(
        f'INSERT INTO {TABELA} '
        '(nome, idade, numero, sexo, senha) '
        'VALUES (?, ?, ?, ?, ?)',
        [nome, idade, numero, sexo, senha]
    )
    conn.commit()


def atualizarDB(opcao_mudar, valor,_id ):
    cursor.execute(
        f'UPDATE {TABELA} '
        f'SET "{opcao_mudar}"= "{valor}"'
        f'WHERE "id" = {_id}'
    )
    conn.commit()
    cursor.close()
    conn.close()

class GuardaVolumes:
    def __init__(self):
        self.aplicacao()
        
    def aplicacao(self):
        print('\033[32mGUARDA VOLUMES OEL!')
        print('BEM VINDO!')
        while True:
            print('Fazer cadastro -> [1]\nEntrar -> [2]\nAlterar informaçoes -> [3]\033[m')
            conn = sqlite3.connect(CAMINHOCPT)
            cursor = conn.cursor()
            while True:
                try:
                    opcao_escolha = int(input('Oque deseja fazer '))
                    break
                except:
                    print('\033[31malgo deu errado\033[m]')
    
            if opcao_escolha == 1:
                def senha():
                    letras = string.ascii_letters
                    numeros =  string.digits
                    tres_letras = sr().choices(letras,k=3)
                    tres_numeros = sr().choices(numeros,k=3)
                    senha = ''.join(tres_letras + tres_numeros)
                    return senha
                password = senha()
                print('FAZER CADASTRO...')
                while True:
                    nome = input('Nome: ').strip()
                    if nome == '':
                        print('\033[31mtente novamente\033[m')
                    else:
                        break
                while True:
                    try:
                        idade = int(input('Idade: '))
                        break
                    except:
                        print('\033[31mErro\033[m')
                
                while True:
                    try:
                        numero = int(input('Numero Tel: '))
                        break
                    except:
                        print('\033[31mErro\033[m')

                while True:
                    sexo = input('Sexo: ').strip()
                    if sexo == '':
                        print('\033[31mtente novamente\033[m')
                    else:
                        break
                print('Senha Gerada automaticamente.')
                print(f'Sua Senha de acésso: {password}')
                adicionarTab(nome,idade,numero,sexo,password)
                print('Success')
                print()
            
            elif opcao_escolha == 2:
                print()
                print('esqueci minha senha -> [1]\ncontinuar -> [2]')
                while True:
                    try:
                        confirmacao = int(input(''))
                        break
                    except:
                        print('\033[31malgo deu errado\033[m]')
                if confirmacao == 2:
                    password_verificacao = input('Senha de acesso: ')
                    cursor.execute(f'SELECT * FROM {TABELA} ')
                    for row in cursor.fetchall():
                        _id,nome,idade,numero, sexo, senha = row
                        if password_verificacao == senha:
                            print('Dados cliente:')
                            print(f'{_id} {nome} {idade:.0f} {numero:.0f} {sexo} {senha}')
                            print()
                elif confirmacao == 1:
                    cursor.execute(f'SELECT * FROM {TABELA}')
                    recuperacao = input('nome: ')
                    for informacao in cursor.fetchall():
                        _id,nome,idade,numero,sexo,senha = informacao
                        if recuperacao == nome:
                            nova_senha = input('Nova senha: ')
                            print('SENHA ALTERADA')
                            print()
                            cursor.execute(f'UPDATE {TABELA} '
                                        f'SET "senha"= {nova_senha} '
                                        f'WHERE "id"= {_id}'
                                        )
                            conn.commit()
                            

            elif opcao_escolha == 3:
                print('ALTERAR CADASTRO!')
                alterar = input('SENHA, PARA ALTERAR INFORMAÇÕES: ')
                cursor.execute(f'SELECT * FROM {TABELA}')
                for inf in cursor.fetchall():
                    _id, nome, idade,numero, sexo, senha, = inf
                    if alterar in senha:
                        print('oque deseja mudar?')
                        print('nome, idade, numero, sexo, senha')
                        opcao_mudar = input('Escolha: ')
                        valor = input('Nova informação: ')
                        senha_conf = _id
                        print('Alteração Concluida')
                        print()
                        atualizarDB(opcao_mudar, valor,senha_conf)
                        
v = GuardaVolumes()