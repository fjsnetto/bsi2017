# -*- coding: utf-8 -*-
'''
Created on 16 de mar de 2017

@author: Aluno
'''


print 'Quantos alunos tem na turma?'
numAlu = input()
print 'Quantas notas cada aluno tem?'
numNot = input()
print 'Qual a média para aprovação?'
media = input()

listaAprovados = ''
listaRecuperacao = ''
mediaAluno = 0
somaMedia = 0
maiorMedia = 0
menorMedia = 9999
soma = 0

for i in range(0, numAlu): 
    nomeAluno = raw_input('Digite o nome do aluno')
    
    for k in range(0, numNot):
        nota = input('Qual a nota do aluno?')
        soma = soma + nota
    
    mediaAluno = soma*1.0 / numNot
    somaMedia = somaMedia + mediaAluno
    
    if mediaAluno > maiorMedia:
        maiorMedia = mediaAluno
        print 'Maior média atualizada'
    
    if mediaAluno < menorMedia:
        menorMedia = mediaAluno
        print 'Menor média atualizada'
    
    if mediaAluno < media:
        listaRecuperacao = listaRecuperacao + nomeAluno + ':' + str(mediaAluno) + ' ; '
    else:
        listaAprovados = listaAprovados + nomeAluno + ':' + str(mediaAluno) + ' ; '
        
    mediaAluno = 0
    soma = 0
    
print 'Alunos aprovados:', listaAprovados
print 'Alunos em recuperação:' , listaRecuperacao
print 'Média da turma:' , round(somaMedia / numAlu, 2) ,
print 'Maior média:' , maiorMedia , 'e menor média:' , menorMedia