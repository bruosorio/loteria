"""
Ainda não sei pq não roda direto aqui no Solo Learn, se alguem souber, me avise!
Rio 16/04/2017
BO
"""

from random import randint
from math import factorial

listnums = []
listjogos = []
countpos = 0
jogosrep = 0


def limitecombina(a, b):
    num = factorial(a) / (factorial(b) * factorial(a - b))
    return num


print('Bem vindo ao sistema de gereação de Jogos!')

numpos = int(input('Quantos números por Jogo:')) - 1
minimo = int(input('Menor valor a ser jogado:'))
maximo = int(input('Maior valor a ser jogado:'))
numelementos = maximo - minimo
limite = int(limitecombina(numelementos, numpos))
print('Voce só pode jogar até o limite de', limite, 'jogo(s)')
numjogos = int(input('Quantidade de Jogos:'))


while numjogos > limite:
    print("O numero de jogos não pode ultrapassar o limite, digite nivamente")
    numjogos = int(input('Quantidade de jogos:'))

while maximo < numpos:
    print('O Maior número não pode ser menor que a quantidade de números por jogo')
    maximo = int(input('Maior valor a ser jogado:'))

while len(listjogos) <= numjogos - 1:
    while len(listnums) <= numpos:
        numescolha = randint(minimo, maximo)
        if numescolha in listnums:
            numescolha = randint(minimo, maximo)
        else:
            listnums.insert(countpos, numescolha)
            countpos + 1
    listnums.sort()
    if listnums in listjogos:
        listnums = []
        jogosrep = jogosrep + 1
    else:
        listjogos.append(listnums)
        listnums = []

listjogos.sort()

print('Esses são os números:')
print('Foram Gerados e Excluidos', jogosrep, 'Jogos Repetidos')
print(*listjogos, sep="\n")
