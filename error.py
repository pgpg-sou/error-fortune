#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import Connection
import random

con = Connection('localhost', 27017)

kekka = [{'un' : 'daikichi', 'result' : u'このエラーを出したあなた！今年の運勢は最高！！神wwwwwすげぇwwww'}, \
			{'un' : 'chukichi', 'result' : u'このエラーをだしたあなたの運勢は高め！！今年も良い一年になるんじゃないですかねぇ…はい…'}, \
			{'un' : 'kichi', 'result' : u'このエラーを出したあなたの運勢は普通。。。うん。。。ふ、普通っていい響きだよね！うん！'}, \
			{'un' : 'kyo', 'result' : u'このエラーを出したあなたの運勢は低め…てかまぁ仕方ないよね、エラーなんて出したくて出してるわけじゃないしね、気を持ってどんどんエラーに挑戦しましょう！！！'}, \
			{'un' : 'daikyo', 'result' : u'こんな初歩的なエラーを出したあなたの今年の運勢は最悪！！てかそれくらいのエラー基本的に回避できるっしょwwwww情弱wwwwwwワロwwwwwwwwうはwwwwwww'}]

db = con.uranai
col = db.uranai

col.remove()

for line in open('error.txt', 'r'):
	itemList = line[:-1]
	if itemList == 'SyntaxError':
		col.insert({ 'error' : itemList, \
					'un' : kekka[4]['un'], \
					'result' : kekka[4]['result']})
	else :
		select = random.randint(0, 4)
		col.insert({ 'error' : itemList, \
					'un' : kekka[select]['un'], \
					'result' : kekka[select]['result']})
