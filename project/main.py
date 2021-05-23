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
	for i, v in pairs(codes):
		table.append([alphabet[i], v])
	return table

def GenTest(train, TN=None):
	rs = []

	n1 = int(TN and TN[0] or CONFIG['TASKS_1'])
	n2 = int(TN and TN[1] or CONFIG['TASKS_2'])
	n3 = int(TN and TN[2] or CONFIG['TASKS_3'])

	for _ in range(n1):
		toFill = [randint(1, 20), randint(1, 10)]
		t = {
			'answer': None,
			'question': {
				'text': 'Некоторый язык состоит из {0} букв. Сколько различных {1}-буквенных слов можно образовать в этом языке?'.format(*toFill)
			}, 
			'correctAnswer': str(toFill[0] ** toFill[1])
		}
		rs.append(t)
	for _ in range(n2):
		table = EncTable(randint(0, CONFIG['T2_ALPH_SZ'] - 1))
		sQ, sA = [], []
		for _ in range(5, CONFIG['T2_MAXLEN'] + 1):
			i = randint(0, len(table) - 1)
			sQ.append(table[i][1])
			sA.append(table[i][0])
		t = {
			'answer': None,
			'question': {
				'text': 'Раскодируйте следующую строку по данной таблице:',
				'expr': ' '.join(sQ),
				'table': table
			},
			'correctAnswer': ''.join(sA)
		}
		rs.append(t)
	for _ in range(n3):
		s = RandomByteStr(CONFIG['T3_BYTES'])
		t = {
			'answer': None,
			'question': {
				'text': 'Закодируйте следующие биты кодом Хемминга:',
				'expr': str(hem.chars_to_bin(s))
			}, 
			'correctAnswer': hem.encode(s)
		}
		rs.append(t)

	if not train:
		for i in range(len(rs)):
			rs[i]['correctAnswer'] = None
	return rs

def RandomByteStr(bytes):
	return ''.join([chr(randint(0, 255)) for i in range(bytes)])


pprint(GenTest(True, [1, 1, 1]))