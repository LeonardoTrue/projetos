"""
sistema de aluguel de estacionamento
registrar hora de entrada e hora de saida
cobrar por hora de permanencia
somar valor baseado no valor hora do estacionamento
(hora de saida linha 57 é penas uma data criada para testes
caso mude para data real do sistema, necessario alterar formatação na linha 58)
"""
from datetime import datetime


class Estacionamento:
    def __init__(self):
        self.valor_hora = 15
        self.cadastrocarro()

    def cadastrocarro(self):
        car = {}
        lista = []
        f = '%d/%m/%Y %H:%M'
        print('Aluguel de estacionamento Quiabo R$ 15,00 a Hora')
        print('[1] CADASTRAR VEICULOS')
        print('[3] Ver Veiculos')
        print('[4] Dar Baixa')
        while True:
            while True:
                try:
                    op = int(input('Opção: '))
                    if op == 1:
                        placa = input('Placa do Veiculo ')
                        nome = input('Nome do Titular ')
                        hora_entrada = datetime.now()
                        car["Placa"] = placa
                        car["Nome"] = nome
                        car["entrada"] = hora_entrada
                        lista.append(car.copy())
                        car.clear()
                        print(lista)
                    # elif op == 2:
                    #     break
                    elif op == 3:
                        for i, dado in enumerate(lista):
                            print(i, dado)
                    elif op == 4:
                        while True:
                            try:
                                procurar_placa = input('Placa do Veiculo ')
                                break
                            except:
                                print('Algo deu errado Tente novamente')
                        print()
                        for i, dado in enumerate(lista):
                            if procurar_placa in lista[i]['Placa']:
                                APENAS_FORMATACAO_ENTRADA = lista[i]['entrada'].strptime(str(lista[i]['entrada']), '%Y-%m-%d %H:%M:%S.%f')
                                APENAS_FORMATACAO_ENTRADA = APENAS_FORMATACAO_ENTRADA.strftime(f)
                                hora_test = datetime(2023, 4, 9, 22, 59)
                                APENAS_FORMATACAO_SAIDA = hora_test.strptime(str(hora_test),'%Y-%m-%d %H:%M:%S')
                                APENAS_FORMATACAO_SAIDA = APENAS_FORMATACAO_SAIDA.strftime(f)

                                h_entrada = lista[i]['entrada'].hour
                                h_saida = hora_test.hour
                                quantidade_horas = h_saida - h_entrada
                                cauculando_custo_estacionamento = quantidade_horas * self.valor_hora
                                print(f'\033[32mPermanencia e custo Total\n'
                                      f'Horario de Entrada: {APENAS_FORMATACAO_ENTRADA}\n'
                                      f'Horario de Saida: {APENAS_FORMATACAO_SAIDA}\n'
                                      f'Você Permaneceu {quantidade_horas} Horas\n'
                                      f'Valor Total R$ {cauculando_custo_estacionamento:,.2f}\033[m')

                    break
                except:
                    print('Algo saiu errado Tente novamente')


Estacionamento()

