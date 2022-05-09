print('~' * 25)
print('CONVERSOR DE BASES')
print('~' * 25)
escolha = 0
bin = octa = hexa = ''
numero = int(input('Insira um número de base decimal para ser convertido: '))
numerosalvo = numero
while True:
    escolha = int(input('''Escolha uma opção:

1 - Conversão para binário.
2 - Conversão para octal.
3 - Conversão para hexadecimal.
4 - Escolher novo número.
5 - Sobre.
6 - Sair.

Sua escolha: '''))
    if escolha == 1:
        while numero > 0:
            bin = str(numero % 2) + bin
            numero = numero // 2
        numero = numerosalvo
        print('~' * 20)
        print(f'Conversão para binário: {bin}')
        print('~' * 20)
        bin = ''
    elif escolha == 2:
        while numero > 0:
            octa = str(numero % 8) + octa
            numero = numero // 8
        numero = numerosalvo
        print('~' * 20)
        print(f'Conversão para octal: {octa}')
        print('~' * 20)
        octa = ''
    elif escolha == 3:
        while numero > 0:
            if (numero % 16) == 10:
                hexa = 'A' + hexa
            elif (numero % 16) == 11:
                hexa = 'B' + hexa
            elif (numero % 16) == 12:
                hexa = 'C' + hexa
            elif (numero % 16) == 13:
                hexa = 'D' + hexa
            elif (numero % 16) == 14:
                hexa = 'E' + hexa
            elif (numero % 16) == 15:
                hexa = 'F' + hexa
            else:
                hexa = str(numero % 16) + hexa
            numero = numero // 16
        numero = numerosalvo
        print('~' * 20)
        print(f'Conversão para hexadecimal: {hexa}')
        print('~' * 20)
        hexa = ''
    elif escolha == 4:
        numero = int(input('Insira um novo número para ser convertido: '))
        numerosalvo = numero
        print(f'O novo número escolhido é {numero}.')
    elif escolha == 5:
        print('''
        Desenvolvido por:
        
        Gustavo Nunes - gustavompn06@gmail.com
        ''')
    elif escolha == 6:
        break
    else:
        print('\033[1;91mPor favor, escolha a opção digitando um número de 1 a 6.\033[0;0m')
