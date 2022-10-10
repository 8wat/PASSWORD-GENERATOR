import random as rd

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!$%&/\<>()=?¿^*'

unidos = f'{letras}{numeros}{simbolos}'

password = ''.join(rd.sample(unidos,14))

print(password)


#8wat :)
