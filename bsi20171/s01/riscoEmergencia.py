# -*- coding: utf-8 -*-
'''
Created on 26 de mar de 2017

@author: Francisco
'''

vermelho = 0
emergencia = False
amarelo = 0
urgencia = False
verde = 0
naoUgencia = False

# Verificacao de emergencia
pulso = input('Informe o pulso do paciente')
paDiastoica = input('Informe a pressao arterial diastoica')
paSistoica = input('informe a pressao arterial sistoica')
fr = input('Informe a frequencia respiratoria')

if pulso < 45 or pulso > 140:
    vermelho = vermelho +1
if paDiastoica < 130:
    vermelho = vermelho +1
if paSistoica < 80:
    vermelho = vermelho +1
if fr < 10 or fr > 34:
    vermelho = vermelho +1
if vermelho >= 2:
    emergencia = True
    print 'Paciente em emergência, requer intervenção médica imediata'
else: # Verificacao de urgencia
    fc = input('Informe a frequencia cardiaca do paciente')
    temperatura = input('Informe a temperatrura do paciente')
    if fc < 50 or fc > 140:
        amarelo = amarelo +1
    if paSistoica < 90 or paSistoica > 240:
        amarelo = amarelo +1
    if paDiastoica > 130:
        amarelo = amarelo +1
    if temperatura < 35 or temperatura > 40:
        amarelo = amarelo +1
    if amarelo >= 2:
        urgencia = True
        print 'Paciente em estado de urgência, requer atendimento prioritário'
    else:  # Verificacao de semi urgencia
        print 'Responda Sim ou Não para as perguntas seguintes. Use 0-Não e 1-Sim'
        idade = input('O paciente tem mais de 60 anos? 0 ou 1?')
        gestante = input('É gestante com complicações na gravidez?')
        deficiente = input('É deficiente físico?')
        retorno = input('É um retorno com menos de 24 horas devido a não melhora?')
        deambulacao = input('Impossibilidade de deambulação?')
        asma = input('Asma fora de crise?')
        enxaqueca = input ('Enxaqueca? Paciente com diagnóstico anterior de enxaqueca')
        if idade or gestante:
            semiUrgencia = True
            print 'Paciente em estado de semi urgencia, requer atendimento em até 01 hora'
        else:
            if deficiente:
                verde = verde +1
            if retorno:
                verde = verde +1
            if deambulacao:
                verde = verde +1
            if asma:
                verde = verde +1
            if enxaqueca:
                verde = verde +1
            if verde >= 2:
                semiUrgencia = True
                print 'Paciente em estado de semi urgencia, requer atendimento em até 01 hora'
            else: 
                print 'Paciente em estado de não urgencia, atendimento por ordem de chegada'
        
        
        
