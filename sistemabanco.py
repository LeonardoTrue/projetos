from abc import ABC,abstractmethod
from time import sleep

class Conta(ABC):
    @abstractmethod
    def contaclient(self, numero, agencia):
       return (numero, agencia)


class Poupanca(Conta):
    def __init__(self):
        self.saldo = 0

    def contaclient(self, numero, agencia):
        return (numero, agencia)

    def depositar(self):
        while True:
            try:
                dep = float(input('\033[32mValor do deposito:\033[m '))
                if dep <= 0:
                    print('\033[31mValor nao Suportado, digite um Valor!\033[m')
                    continue
                else:
                    self.saldo += dep
                    print('\033[36mDeposito Realizado\033[m')
            except:
                print('\033[31mAlgo deu errado, Tente novamento\033[m')
            break


    def sacar(self):
        while True:
            try:
                valor = float(input('\033[32mValor do Saque:\033[m '))

                if valor > self.saldo:
                    print('\033[31mSaldo insuficiente!\033[m')
                    break
                else:
                    self.saldo -= valor
                    print(f'\033[32mSaque Realizado R${valor:,.2f}\033[m')
                    break
            except:
                print('\033[31mAlgo saiu errado, tente novamente!\033[m ')


class Corrente(Conta):
    def __init__(self):
        self.saldo = 0

    def contaclient(self, numero, agencia):
        return (numero, agencia)


    def depositar(self):
        while True:
            try:
                dep = float(input('\033[32mValor do deposito:\033[m '))
                if dep <= 0:
                    print('\033[31mValor nao Suportado, digite um Valor!\033[m')
                    continue
                else:
                    self.saldo += dep
                    print('\033[32mDeposito efetuado')
                    if self.saldo < -9999999999:
                       self.saldo -= dep
                break
            except:
                print('\033[31mAlgo deu errado, Tente novamento\033[m')
            break

    def sacar(self):
        while True:
            try:
                valor = float(input('\033[32mValor do Saque:\033[m '))
                if valor > self.saldo:
                    print('''\033[33mvoce nao tem limite, se prosseguir, ficará com saldo negativo''')
                    print('[1] Sim')
                    print('[2] Nao\033[m')
                    while True:
                        try:
                            confi = int(input('\033[33mdeseja prosseguir:\033[m '))
                            if confi == 1:
                                self.saldo -= valor
                                print(f'\033[32memprestimo de R${valor:,.2f} CONFIRMADO\033[m')
                                print()
                                break
                            elif confi == 2:
                                break
                        except:
                            print('\033[31mAlgo saiu Errado! Tente novamente\033[m')
                else:
                    self.saldo -= valor
                    print(f'\033[32mR${valor:,.2f} Sacado! Saldo restante: R${self.saldo:,.2f}\033[m')
                    break

            except:
                print('\033[31mAlgo deu Errado, Tente novamente!\033[m')
            break


class Banco:
    def __init__(self):
        self._contaC = Corrente()
        self._poupaca = Poupanca()


    def operacao_contaCorrente(self):
        lista = []
        while True:
            print('\033[34mBANCO TACTAC')
            print('Adicione Sua Conta TAC')
            print('Voce tem conta?')
            print('[1] Sim')
            print('[2] Nao')
            print('[3] Voltar\033[m')
            while True:
                try:
                    op = int(input('escolha: '))
                    break
                except:
                    print('\033[31mAlgo deu errado, Tente Novamente\033[m ')
            sleep(1.5)
            print()
            if op == 3:
                break
            if op == 2:
                conta = int(input('Digite a conta: '))
                agencia = int(input('Digite a agencia: '))
                print('\033[32mSuccess\033[m')
                print()
                ctcliente = self._contaC.contaclient(conta, agencia)
                lista.append(ctcliente)
                sleep(1.5)
            if op == 1:
                while True:
                    try:
                        conta = int(input('Digite a conta: '))
                        break
                    except:
                        print('Algo saiu errado, tente novamente')
                while True:
                    try:
                        agencia = int(input('Digite a agencia: '))
                        break
                    except:
                        print('Algo saiu errado, tente novamente')
                print()
                try:
                    print(f'Conta: Corrente: {lista[0]}')
                except:
                    print('Conta nao encontrada')
                sleep(1.5)
                for i, v in enumerate(lista):
                    if conta in lista[i] and agencia in lista[i]:
                        while True:
                            print('\033[35mo que deseja Fazer hoje?')
                            print('depositar -> [1]')
                            print('sacar -> [2]')
                            print('Ver Saldo -> [3]')
                            print('Voltar -> [4]\033[m')
                            while True:
                                try:
                                    escolha = int(input('opção: '))
                                    sleep(1.5)
                                    break
                                except:
                                    print('\033[31mAlgo saiu errado, Tente Novamente\033[m')
                            if escolha == 1:
                                self._contaC.depositar()
                            elif escolha == 2:
                                self._contaC.sacar()
                            elif escolha == 3:
                                print(f'\033[32mSALDO:{self._contaC.saldo:,.2f}\033[m')
                            elif escolha == 4:
                                break
                    else:
                        print('errr')


    def operacao_contaPoupanca(self):
        lista = []
        while True:
            print('\033[34mBANCO TACTAC')
            print('Adicione Sua Conta TAC')
            print('voce tem conta?')
            print('[1] Sim')
            print('[2] Nao')
            print('[3] Voltar\033[m')
            while True:
                try:
                    op = int(input('escolha: '))
                    sleep(1.5)
                    break
                except:
                    print('\033[31mAlgo saiu errado, Tente Novamente\033[m')
            print()
            if op > 3:
                print('\033[31mOPÇAO INVALIDA\033[m')
            if op == 3:
                break

            if op == 2:
                while True:
                    try:
                        conta = int(input('Digite a conta: '))
                        break
                    except:
                        print('\033[31mAlgo saiu errado, tente novamente\033[m')
                while True:
                    try:
                        agencia = int(input('Digite a agencia: '))
                        sleep(1.5)
                        break
                    except:
                        print('\033[31mAlgo saiu errado, tente novamente\033[m')
                print('\033[32mSuccess\033[m')
                print()
                ctcliente = self._poupaca.contaclient(conta, agencia)
                lista.append(ctcliente)
            if op == 1:
                while True:
                    try:
                        conta = int(input('Digite a conta: '))
                        break
                    except:
                        print('\033[31mAlgo saiu errado, tente novamente\033[m')
                while True:
                    try:
                        agencia = int(input('Digite a agencia: '))
                        sleep(1.5)
                        break
                    except:
                        print('\033[31mAlgo saiu errado, tente novamente\033[m')
                print()
                for i, v in enumerate(lista):
                    if conta in lista[i] and agencia in lista[i]:
                        try:
                            print(f'Conta: Poupança: {lista[0]}')
                        except:
                            print('Conta nao encontrada')
                        while True:
                            print('\033[35moque deseja Fazer hoje?')
                            print('depositar -> [1]')
                            print('sacar -> [2]')
                            print('Ver Saldo -> [3]')
                            print('Voltar -> [4]\033[m')
                            while True:
                                try:
                                    escolha = int(input('opção: '))
                                    sleep(1.5)
                                    break
                                except:
                                    print('\033[31mAlgo saiu errado, Tente Novamente\033[m')
                            if escolha == 1:
                                self._poupaca.depositar()
                            elif escolha == 2:
                                self._poupaca.sacar()
                            elif escolha == 3:
                                print(f'\033[32mSALDO:{self._poupaca.saldo:,.2f}\033[m')
                            elif escolha == 4:
                                break


def escolher_conta_de_uso(conta: Banco):
    while True:
        print('Qual conta deseja Usar?')
        print('[ 1 ] Conta Corrente')
        print('[ 2 ] Conta Poupança')
        print('[ 3 ] Fechar')
        conta_escolhida = int(input('Conta: '))
        if conta_escolhida == 1:
            print('\033[32mProcessando...\033[m')
            sleep(2)
            aqui_uso_a_contaC = conta.operacao_contaCorrente()
        elif conta_escolhida == 2:
            print('\033[32mProcessando...\033[m')
            sleep(2)
            aqui_uso_a_contaP = conta.operacao_contaPoupanca()
        elif conta_escolhida == 3:
            print('\033[33mFinalizando...\033[m')
            sleep(2.5)
            break


b = Banco()
escolher_conta_de_uso(b)
print('\033[32mOBRIGADO VOLTE SEMPRE!\033[m')
