import seletor_funcoes_memorias
import seletor_funcoes_4
import seletor_funcoes_3
import seletor_funcoes_2
import seletor_funcoes_1
import funcoes
import memoria

class Saica():
    
    def __init__(self):
        Saica.Resposta(Saica, '-----------S.A.I.C.A--------------')
        while True:    
         #   try:
                #Entrada
                FraseUser, ListPalavras = Saica.Entrada(Saica)
                #Pensa
                resp = Saica.Pensa(Saica, FraseUser, ListPalavras)
                #Saída
                respFinal, YX = Saica.Resposta(Saica, resp)
                
                #Desligamento
                if YX == 'Y':
                    break
        
            #Se ocorrer um erro
          #  except:
           #     Saica.Resposta(Saica, 'Temos um problema...')
        
        
    def Entrada(self):
        fraseUser = input(': ')
        
        #Filtro conversor
        fraseUser = fraseUser.lower()
        fraseUser = fraseUser.replace(',',' ')
        fraseUser = fraseUser.replace('?',' ?')
        fraseUser = fraseUser.replace('.',' ')
        fraseUser = fraseUser.replace('!',' ')
        ListPalavras = fraseUser.split()
        return fraseUser, ListPalavras


    def Pensa(self, fraseUser, ListPalavras):
        
            #Memorizando Entradas
            memoria.memorizarEntradas(fraseUser)
        
            #Processando a Resposta
            resposta = seletor_funcoes_4.SeletorFuncoes_4(ListPalavras) 
            if resposta == None:
                resposta = seletor_funcoes_3.SeletorFuncoes_3(ListPalavras)
            if resposta == None:
                resposta = seletor_funcoes_2.SeletorFuncoes_2(ListPalavras)
            if resposta == None:
                resposta = seletor_funcoes_1.SeletorFuncoes_1(ListPalavras)
            if resposta == None:
                resposta = funcoes.saicaCalc(fraseUser)
            if resposta == None:
                resposta = seletor_funcoes_memorias.SeletorFuncoesMemorias()
                                    
            return resposta
    

    def Resposta(self, resposta):
        
            if resposta == None:
                resposta = "..."
            try:
                if resposta[1] == None:
                    resposta = resposta[0]
            except:         
                pass
            
            #Memorizando Respostas
            memoria.memorizarRespostas(resposta)
            #Função de Desligar
            resp = memoria.LembrarFuncoes()
            if resp[-1] == "funcoes.desligar()":
                memoria.ApagarMemoriaEntradas()
                memoria.ApagarMemoriaRespostas()
                memoria.ApagarMemoriaFuncoes()
                return print(str(resposta)),'Y'
            
            return print(str(resposta)),'X'