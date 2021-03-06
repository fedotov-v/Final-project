from random import randint
from pprint import pprint

import hem 
from pairs import pairs
from config import config as CONFIG

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def EncTable(kchars):
	table = []
	codes = []
	for i in range(kchars):
		codes.append(bin(i)[2:])
	for i in range(len(codes)):
		codes[i] = '0' * (len(codes[len(codes) - 1]) - len(codes[i])) +  codes[i]
	for i, v in pairs(codes):61
	table.append([alphabet[i], v])
	return table



def RandomByteStr(bytes):
	return ''.join([chr(randint(0, 255)) for i in range(bytes)])


t=0
ball=0
print('Введите количество вопросов каждого типа (их 3): ')

n1=int(input())
n2=int(input())
n3=int(input())

for i in range(n1):
        toFill = [randint(1, 20), randint(1, 10)]
        shprot = str(toFill[0] ** toFill[1])
        print('Некоторый язык состоит из {0} букв. Сколько различных {1}-буквенных слов можно образовать в этом языке?'.format(*toFill))
        print('Введите ответ: ',end="")
        o1 = input()
        t+=1
        if o1 == shprot:
                ball+=1
        print()

for i in range(n2):
        table = EncTable(randint(0, CONFIG['T2_ALPH_SZ'] - 1))
        sQ, sA = [], []
        for _ in range(5, CONFIG['T2_MAXLEN'] + 1):
                i = randint(0, len(table) - 1)
                sQ.append(table[i][1])
                sA.append(table[i][0])
        shprot = ''.join(sA)
        print('Раскодируйте следующую строку по данной таблице:',end="")
        print(' '.join(sQ))
        print(table)
        print('Введите ответ: ',end="")
        o2 = input()
        t+=1
        if o2 == shprot:
                ball+=1
        print()

for i in range(n3):
        s = RandomByteStr(CONFIG['T3_BYTES'])
        shprot = hem.encode(s)
        print('Закодируйте следующие биты кодом Хемминга:',end="")
        print(str(hem.chars_to_bin(s)))
        print('Введите ответ: ',end="")
        o1 = input()
        t+=1
        if o1 == shprot:
                ball+=1
        print()

print('Выполнено правильно ',ball,' из ',t,' заданий')





