import json

#Memoria

#Consultar Histórico de Entradas
def LembrarEntradas():
    try:
        # Lendo e carregando os dados do "arquivo.json" para uma variável no python.
        arquivo_leitura = open('memoria_entradas'+'.json','r')
        arquivo_leitura_carregado = json.load(arquivo_leitura)
        arquivo_leitura.close()
        return arquivo_leitura_carregado
    except:
        return ['n']

#Memorizar Entradas
def memorizarEntradas(entrada):
    #Lendo e carregando os dados do "arquivo.json" para uma variável no python.
    arquivo_leitura = open('memoria_entradas'+'.json','r')
    arquivo_leitura_carregado = json.load(arquivo_leitura)
    arquivo_leitura.close()
    
    #juntando os dados carregados do "arquivo.json" e a informação da variável "nome".
    arquivo_leitura_carregado.append(entrada)
    arquivo_escrita= open('memoria_entradas'+'.json','w')
    json.dump(arquivo_leitura_carregado, arquivo_escrita)
    arquivo_escrita.close()

#Apagar Memoria Entradas
def ApagarMemoriaEntradas():
    # juntando os dados carregados do "arquivo.json" e a informação da variável "nome".
    arquivo_leitura_carregado = ["","",""]
    arquivo_escrita= open('memoria_entradas'+'.json','w')
    json.dump(arquivo_leitura_carregado, arquivo_escrita)
    arquivo_escrita.close()

#-----------------------------------------------------------------------------

#Consultas Histórico de Respostas
def LembrarRespostas():
    try:
        # Lendo e carregando os dados do "arquivo.json" para uma variável no python.
        arquivo_leitura = open('memoria_respostas'+'.json','r')
        arquivo_leitura_carregado = json.load(arquivo_leitura)
        arquivo_leitura.close()
        return arquivo_leitura_carregado
    except:
        return ['n']

#Memorizar Respostas
def memorizarRespostas(resposta):
    #Lendo e carregando os dados do "arquivo.json" para uma variável no python.
    arquivo_leitura = open('memoria_respostas'+'.json','r')
    arquivo_leitura_carregado = json.load(arquivo_leitura)
    arquivo_leitura.close()
    
    #juntando os dados carregados do "arquivo.json" e a informação da variável "nome".
    arquivo_leitura_carregado.append(resposta)
    arquivo_escrita= open('memoria_respostas'+'.json','w')
    json.dump(arquivo_leitura_carregado, arquivo_escrita)
    arquivo_escrita.close()
    pass

#Apagar Memoria Respostas
def ApagarMemoriaRespostas():
    # juntando os dados carregados do "arquivo.json" e a informação da variável "nome".
    arquivo_leitura_carregado = ["","",""]
    arquivo_escrita= open('memoria_Respostas'+'.json','w')
    json.dump(arquivo_leitura_carregado, arquivo_escrita)
    arquivo_escrita.close()

#------------------------------------------------------------------------------

#Consultas Histórico de Funcoes
def LembrarFuncoes():
    try:
        # Lendo e carregando os dados do "arquivo.json" para uma variável no python.
        arquivo_leitura = open('memoria_funcoes'+'.json','r')
        arquivo_leitura_carregado = json.load(arquivo_leitura)
        arquivo_leitura.close()
        return arquivo_leitura_carregado
    except:
        return ['n']

#Memorizar Funcoes usadas
def memorizarFuncoes(resposta):
    #Lendo e carregando os dados do "arquivo.json" para uma variável no python.
    arquivo_leitura = open('memoria_funcoes'+'.json','r')
    arquivo_leitura_carregado = json.load(arquivo_leitura)
    arquivo_leitura.close()
    
    #juntando os dados carregados do "arquivo.json" e a informação da variável "nome".
    arquivo_leitura_carregado.append(resposta)
    arquivo_escrita= open('memoria_funcoes'+'.json','w')
    json.dump(arquivo_leitura_carregado, arquivo_escrita)
    arquivo_escrita.close()
    pass

#Apagar Memoria Respostas
def ApagarMemoriaFuncoes():
    # juntando os dados carregados do "arquivo.json" e a informação da variável "nome".
    arquivo_leitura_carregado = ["","",""]
    arquivo_escrita= open('memoria_funcoes'+'.json','w')
    json.dump(arquivo_leitura_carregado, arquivo_escrita)
    arquivo_escrita.close()