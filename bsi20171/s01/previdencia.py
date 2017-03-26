# -*- coding: utf-8 -*-
'''
Created on 18 de mar de 2017

@author: Francisco
'''

valBeneficio = 0.0
percentualContrib = 0.0

nome = raw_input('Informe seu nome')
idade = input('Informe sua idade')
nMeses = input('Informe a quantidade de meses de contribuição')
salContrib = input('Informe o valor do seu salário de contribuição')

if idade >= 65 and nMeses >= 300:
    percentualContrib = (nMeses / 12) + 51.0
    if percentualContrib > 100:
        percentualContrib = 100.0

    valBeneficio = (percentualContrib / 100) * salContrib
    print 'O valor do seu beneficio será de:' , valBeneficio
else:
    print 'Você não tem a idade e/ou tempo de contribuição mínimo'