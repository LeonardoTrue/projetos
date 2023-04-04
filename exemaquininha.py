from time import sleep


class Cartao:
    def __init__(self):
        self.credito = 2500
        self.debito = 1500


class Maquina(Cartao):
    def passar_cartao_credito(self, valor):
        if valor <= self.credito:
            print('Compra Realizada com sucesso!')
            print()
            self.credito -= valor
        else:
            print('Saldo insuficiente')
            print(f'Saldo: R$ {self.credito:,.2f}')
            print()
            self.credito = self.credito

    def passar_cartao_debito(self, valor):
        if valor <= self.debito:
            print('Compra Realizada com sucesso!')
            print()
            self.debito -= valor
        else:
            print('Saldo insuficiente')
            print(f'Saldo: R$ {self.debito:,.2f}')
            print()
            self.debito = self.debito

    def maquininha(self):
        while True:
            print('maquininha leoBank:')
            print('insira o Cartao')
            sleep(1)
            print('Processando...')
            sleep(2)
            while True:
                try:
                    valor_da_compra = float(input('Valor da Compra R$: '))
                    break
                except:
                    print('\033[31mDigite um valor Valido\033[m')
            print('OPÇOES DE PAGAMENTO!')
            print()
            print('[ 1 ] Debito')
            print('[ 2 ] Credito')
            while True:
                try:
                    opcao_de_pagamento = int(input('Opção De Pagamento: '))
                    print()
                    break
                except:
                    print('\033[31mDigite apenas numeros!\033[m ')
            if opcao_de_pagamento == 1:
                if self.debito <= 0:
                    print('Voce nao tem Dinheiro o suficiente Para prosseguir!')
                    print(f'Saldo: R$ {self.debito:,.2f}')
                    print('Tente outra forma de pagamento')
                    print()
                if self.debito > 0:
                    print('Forma de Pagamento Debito Escolhido')
                    self.passar_cartao_debito(valor_da_compra)

            elif opcao_de_pagamento == 2:
                if self.credito <= 0:
                    print('Voce nao tem Credito suficiente Para prosseguir!')
                    print(f'Saldo: R$ {self.credito:,.2f}')
                    print('Tente outra forma de pagamento')
                    print()
                if self.credito > 0:
                    print('Forma de Pagamento Credito Escolhido')
                    print('Parcele Suas compras em ate 10x')
                    while True:
                        try:
                            escolher_parcelas = int(input(f'Deseja parcelar O valor R$ {valor_da_compra:,.2f}  \n[1] - SIM\n[2] - NAO \nEscolha: '))
                            break
                        except:
                            print('\033[31mOpçao invalida!\033[m')
                    if escolher_parcelas == 1:
                        while True:
                            try:
                                pagamento_parcelado = int(input('Quantidade de Parcelas: '))
                                print()
                                break
                            except:
                                print('\033[31mDigite a Quantidade de Parcelas\033[m')
                        parcelas = valor_da_compra / pagamento_parcelado
                        if valor_da_compra <= self.credito:
                            print(f'a compra no valor de R$ {valor_da_compra:,.2f} parcelada em {pagamento_parcelado}x\nfica {pagamento_parcelado} parcelas de R$ {parcelas:,.2f}')
                        self.passar_cartao_credito(valor_da_compra)
                    if escolher_parcelas == 2:
                        print()
                        print('Pagamento Credito avista ')
                        self.passar_cartao_credito(valor_da_compra)


maquina = Maquina()
maquina.maquininha()