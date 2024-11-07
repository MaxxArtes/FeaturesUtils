#!/bin/python3

def timeConversion(s):
    hora = s[:2]
    minutos = s[2:8]  # Parte :MM:SS
    periodo = s[-2:]  # "AM" ou "PM"
    
    if periodo == 'AM':
        if hora == '12':
            hora = '00'  # Converte "12 AM" para "00"
    else:  # Caso seja "PM"
        if hora != '12':
            hora = str(int(hora) + 12)  # Converte horas PM exceto "12 PM"
    
    return hora + minutos

if __name__ == '__main__':
    s = input('digite o horario: ').strip()  # Lê a entrada do usuário
    result = timeConversion(s)
    print('seu horario convertido é: ',result)  # Exibe o resultado final sem "\n"
