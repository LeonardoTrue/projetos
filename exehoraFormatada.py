from datetime import datetime


class Relogio:
    def __init__(self):
        self.escolher_formato_hs()

    def escolher_formato_hs(self):
        print('''\033[35m[1] ano/mes/dia hora:minutos:segundo.microsegudos 
[2] dia/mes/ano hora:minutos:segundo.microsegudos        
[3] dia/mes/ano hora:minutos:segundo
[4] dia/mes/ano hora:minutos
[5] dia/mes/ano
[6] Horas:Minutos\033[m''')
        while True:
            h = int(input('Escolha: '))
            if h == 1:
                padrao = '%Y-%m-%d %H:%M:%S.%f'
                # padraoH = datetime.now()
                confdata = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
                novadata = confdata.strftime(padrao)
                print('\033[32mData Local\033[m')
                print(novadata)
                print('ano mes dia horas minutos segundos e microssegundos')

            elif h == 2:
                padrao = '%d-%m-%Y %H:%M:%S.%f'
                # padraoH = datetime.now()
                confdata = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
                novadata = confdata.strftime(padrao)
                print('\033[32mData Local\033[m')
                print(novadata)
                print('dia mes ano horas minutos segundo e microssegundos')

            elif h == 3:
                padrao = '%d-%m-%Y %H:%M:%S'
                # padraoH = datetime.now()
                confdata = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
                novadata = confdata.strftime(padrao)
                print('\033[32mData Local\033[m')
                print(novadata)
                print('dia mes ano horas minutos e segundos')

            elif h == 4:
                padrao = '%d-%m-%Y %H:%M'
                # padraoH = datetime.now()
                confdata = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
                novadata = confdata.strftime(padrao)
                print('\033[32mData Local\033[m')
                print(novadata)
                print('dia mes ano horas minutos')

            elif h == 5:
                padrao = '%d-%m-%Y'
                confdata = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
                novadata = confdata.strftime(padrao)
                print('\033[32mData Local\033[m')
                print(novadata)
                print('dia mes ano')

            elif h == 6:
                padrao = '%H:%M:%S'
                confdata = datetime.strptime(str(datetime.now()), '%Y-%m-%d %H:%M:%S.%f')
                novadata = confdata.strftime(padrao)
                print('\033[32mHora Atual\033[m')
                print(novadata)
            elif h > 6:
                break


h = Relogio()
print('\033[33mVolte Sempre\033[m')