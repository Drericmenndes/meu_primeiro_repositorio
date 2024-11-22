# Sorteador de números
from random import randint as r
from time import sleep as s
print('Vamos fazer um joguinho jovem gafanhoto!')
print('Escolha um número de 0 a 5 e eu lhe direi se esse número é o mesmo que eu sorteei')
usuario=int(input('Escolha um numero entre 0 e 5:'))
print('SORTEANDO...')
s(2)
computador=r(0,5)

if usuario == computador:
    print('parabens!')
else:
    print('voce perdeu, trouxa!')
print(f'O número sorteado foi {computador}')