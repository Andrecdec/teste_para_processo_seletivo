'''
Breve análise:


É possível ver de cara que se trata de um problema de
programação orientada a objeto, portanto definimos as
classes (Funcionario, Projeto e FuncionarioProjeto) e
os atributos (id_ funcionario, nome, uf, ano_nascimento
e etc.) de acordo com as tabelas fornecidas. Na classe
Funcionario, além do método construtor, definimos também
um método para calcular a idade do funcionario, utilizando
o módulo datetime e a função date.


Em seguida, a partir dos dados da tabela de banco de dados,
definimos os objetos com seus respectivos atributos, isto é,
todos os funcionários, todos os projetos e todos os dados
que relacionam os funcionários aos projetos.


Após fazer isso, definimos uma lista de funcionários, uma
lista de projetos e uma lista da relação entre eles.

Depois, criamos um relatório fazendo três tabelas, contemplando
os dados do banco de dados, por meio de três funções. Em seguida,
chamamos as funções. 


Depois, criamos uma lista vazia chamada lista1 e criamos o
loop for para colocar nesta lista vazia as ids dos
funcionários maiores de 20 anos e residentes do Rio de
Janeiro.


Em seguida, criamos uma lista vazia chamada lista2 e criamos
o loop for para colocar nesta lista vazia as ids dos projetos
finalizados.


Criamos uma lista vazia chamada lista3 e criamos o loop for
para colocar nesta lista vazia as ids dos funcionarios que
pertencem a lista 1 e que, por relação com a lista fps,
pertencem a lista2, selecionando assim os funcionarios que
tem mais de 20 anos, residem no Rio de Janeiro e já
trabalharam em projetos finalizados.


Em seguida, utilizamos a função Counter para contar quantos
projetos finalizados cada funcionario havia trabalhado na
lista 3. Definimos a variável c para receber esses dados.
Transformamos c em um tipo dicionário, criamos uma lista
vazia chamada funcionarios_selecionados e criamos um loop for,
usando em seguida um loop if, para colocar nessa lista os
funcionarios que tem mais de 20 anos, residem no Rio de
Janeiro e já trabalharam em mais de 3 projetos finalizados.
Portanto, a lista funcionarios_selecionados guarda as ids dos
funcionarios que foram selecionados a partir dos critérios
pedidos no enunciado.


'''

import datetime
from datetime import date
from collections import Counter

class Funcionario:

    def __init__(self, id_funcionario, nome, uf, ano_nascimento):
        self.id_funcionario = id_funcionario
        self.nome = nome
        self.uf = uf
        self.ano_nascimento = ano_nascimento 
        
    def calcula_idade(self):
        data_atual = date.today()
        idade = data_atual.year - self.ano_nascimento
        return idade
        
class Projeto:
    
    def __init__(self, id_projeto, nome, data_inicio, data_fim):
        self.id_projeto = id_projeto
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        
class FuncionarioProjeto:

    def __init__(self, id_funcionario, id_projeto):
        self.id_funcionario = id_funcionario
        self.id_projeto = id_projeto

fun1 = Funcionario(1,'Funcionário 1', 'RJ',1991)
fun2 = Funcionario(2,'Funcionário 2', 'RJ',1989)
fun3 = Funcionario(3,'Funcionário 3', 'SP',1978)
fun4 = Funcionario(14,'Funcionário 4', 'RJ',2000)
fun5 = Funcionario(15,'Funcionário 5', 'RJ',1996)
fun6 = Funcionario(21,'Funcionário 6', 'MG',1993)
fun7 = Funcionario(23,'Funcionário 9', 'RJ',1999)
fun8 = Funcionario(25,'Funcionário 10', 'RJ',1992)
fun9 = Funcionario(26,'Funcionário 13', 'RJ',1988)

proj1 = Projeto(1,'Projeto 1', [1 ,3 ,2010], [1, 9, 2010])
proj2 = Projeto(2,'Projeto 2', [1, 9, 2011], [1, 9, 2012])
proj3 = Projeto(3,'Projeto 3', [1, 10, 2012], [1, 2, 2013])
proj4 = Projeto(4,'Projeto 4', [1, 8, 2012], [1, 3, 2014])
proj5 = Projeto(5,'Projeto 5', [1, 4, 2013], [1, 12, 2014])
proj6 = Projeto(6,'Projeto 6', [1, 3, 2015], [1, 9, 2016])
proj7 = Projeto(7,'Projeto 9', [1, 6, 2015], [1, 9, 2017])
proj8 = Projeto(8,'Projeto 10', [1, 7, 2016], [])
proj9 = Projeto(9,'Projeto 13', [1, 12, 2017], [])

fp1 = FuncionarioProjeto(1, 2)
fp2 = FuncionarioProjeto(1, 1)
fp3 = FuncionarioProjeto(1, 3)
fp4 = FuncionarioProjeto(1, 4)
fp5 = FuncionarioProjeto(2, 1)
fp6 = FuncionarioProjeto(3, 1)
fp7 = FuncionarioProjeto(14,1)
fp8 = FuncionarioProjeto(3, 4)
fp9 = FuncionarioProjeto(2, 3)

funcionarios = [fun1, fun2, fun3, fun4, fun5, fun6, fun7, fun8, fun9]
projetos = [proj1, proj2, proj3, proj4, proj5, proj6, proj7, proj8, proj9]
fps = [fp1, fp2, fp3, fp4, fp5, fp6, fp7, fp8, fp9]


def TabelaFuncionarios():
    
    print('\n')
    print('\t\tTabela de Funcionários')
    print('--------------------------------------------------------------')
    print("%s\t\t%s\t\t%s\t%s" % ('id_funcionario', 'nome', 'UF', 'Ano de Nascimento'))
    print('--------------------------------------------------------------')
    print("\t%i\t  %s\t\t%s\t%i" % (fun1.id_funcionario, fun1.nome, fun1.uf, fun1.ano_nascimento))
    print("\t%i\t  %s\t\t%s\t%i" % (fun2.id_funcionario, fun2.nome, fun2.uf, fun2.ano_nascimento))
    print("\t%i\t  %s\t\t%s\t%i" % (fun3.id_funcionario, fun3.nome, fun3.uf, fun3.ano_nascimento))
    print("\t%i\t  %s\t\t%s\t%i" % (fun4.id_funcionario, fun4.nome, fun4.uf, fun4.ano_nascimento))
    print("\t%i\t  %s\t\t%s\t%i" % (fun5.id_funcionario, fun5.nome, fun5.uf, fun5.ano_nascimento))
    print("\t%i\t  %s\t\t%s\t%i" % (fun6.id_funcionario, fun6.nome, fun6.uf, fun6.ano_nascimento))
    print("\t%i\t  %s\t\t%s\t%i" % (fun7.id_funcionario, fun7.nome, fun7.uf, fun7.ano_nascimento))
    print("\t%i\t  %s\t%s\t%i" % (fun8.id_funcionario, fun8.nome, fun8.uf, fun8.ano_nascimento))
    print("\t%i\t  %s\t%s\t%i" % (fun9.id_funcionario, fun9.nome, fun9.uf, fun9.ano_nascimento))
    print('\n')


def TabelaProjetos():
    
    
    print('\n')
    print('\t\tTabela de Projetos')
    print('---------------------------------------------------------')
    print("   %s\t   %s\t     %s\t%s" % ('id_projeto', 'Nome', 'Data de Início', 'Data de Fim'))
    print('---------------------------------------------------------')
    print("\t%i\t%s\t%i/%i/%i\t%i/%i/%i" % (proj1.id_projeto, proj1.nome, proj1.data_inicio[0], proj1.data_inicio[1], proj1.data_inicio[2], proj1.data_fim[0], proj1.data_fim[1], proj1.data_fim[2]))
    print("\t%i\t%s\t%i/%i/%i\t%i/%i/%i" % (proj2.id_projeto, proj2.nome, proj2.data_inicio[0], proj2.data_inicio[1], proj2.data_inicio[2], proj2.data_fim[0], proj2.data_fim[1], proj2.data_fim[2]))
    print("\t%i\t%s\t%i/%i/%i\t%i/%i/%i" % (proj3.id_projeto, proj3.nome, proj3.data_inicio[0], proj3.data_inicio[1], proj3.data_inicio[2], proj3.data_fim[0], proj3.data_fim[1], proj3.data_fim[2]))
    print("\t%i\t%s\t%i/%i/%i\t%i/%i/%i" % (proj4.id_projeto, proj4.nome, proj4.data_inicio[0], proj4.data_inicio[1], proj4.data_inicio[2], proj4.data_fim[0], proj4.data_fim[1], proj4.data_fim[2]))
    print("\t%i\t%s\t%i/%i/%i\t%i/%i/%i" % (proj5.id_projeto, proj5.nome, proj5.data_inicio[0], proj5.data_inicio[1], proj5.data_inicio[2], proj5.data_fim[0], proj5.data_fim[1], proj5.data_fim[2]))
    print("\t%i\t%s\t%i/%i/%i\t%i/%i/%i" % (proj6.id_projeto, proj6.nome, proj6.data_inicio[0], proj6.data_inicio[1], proj6.data_inicio[2], proj6.data_fim[0], proj6.data_fim[1], proj6.data_fim[2]))
    print("\t%i\t%s\t%i/%i/%i\t%i/%i/%i" % (proj7.id_projeto, proj7.nome, proj7.data_inicio[0], proj7.data_inicio[1], proj7.data_inicio[2], proj7.data_fim[0], proj7.data_fim[1], proj7.data_fim[2]))
    print("\t%i\t%s\t%i/%i/%i\t\t%s" % (proj8.id_projeto, proj8.nome, proj8.data_inicio[0], proj8.data_inicio[1], proj8.data_inicio[2], '-'))
    print("\t%i\t%s\t%i/%i/%i\t\t%s" % (proj9.id_projeto, proj9.nome, proj9.data_inicio[0], proj9.data_inicio[1], proj9.data_inicio[2], '-'))
    print('\n')

def TabelaFuncionariosProjetos():
    
    print('\n')
    print('  Tabela de Relação entre Funcionários e Projetos')
    print('---------------------------------------------------')
    print("%s\t\t\t\t%s" % ('id_funcionario', 'id_projeto'))
    print('---------------------------------------------------')
    print("\t%i\t\t\t\t%i" % (fp1.id_funcionario, fp1.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp2.id_funcionario, fp2.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp3.id_funcionario, fp3.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp4.id_funcionario, fp4.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp5.id_funcionario, fp5.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp6.id_funcionario, fp6.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp7.id_funcionario, fp7.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp8.id_funcionario, fp8.id_projeto))
    print("\t%i\t\t\t\t%i" % (fp9.id_funcionario, fp9.id_projeto))
    print('\n')

print('\n\n\t\t\tRelatório:')
TabelaFuncionarios()
TabelaProjetos()
TabelaFuncionariosProjetos()




lista1 = []

for i in funcionarios:
    
   t = i.calcula_idade()
   if t > 20:
       
        if i.uf =='RJ':     
            lista1.append(i.id_funcionario)


lista2 = []

for j in projetos:
    
    if j.data_fim != []:
        lista2.append(j.id_projeto)


lista3 = []

for k in fps:
    
    if k.id_funcionario in lista1:
        
        if k.id_projeto in lista2:
            lista3.append(k.id_funcionario)
            

c = Counter(lista3)
c = dict (c)

funcionarios_selecionados = []

for x in c:
    
    if c[x] > 3:
        print (f'O Funcionário de id {x} foi selecionado porque \
tem mais de 20 anos, \nmora no Rio de Janeiro e já trabalhou em mais \
de três projetos finalizados.')    
        funcionarios_selecionados.append(x)
        





            
