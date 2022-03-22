import chaves_funcoes
import funcoes
import memoria

def SeletorFuncoes_1(ListPalavras):

    resposta = chaves_funcoes.ChaveObrigado(ListPalavras)
    if resposta == 1:
        memoria.memorizarFuncoes('funcoes.obrigado()')
        return funcoes.obrigado()
                                                                                      
    if True:
        resposta = chaves_funcoes.ChaveCalculadora(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.calculadora')
            return funcoes.calculadora()
                                                                                    
    if True:
        resposta = chaves_funcoes.ChaveDesligar(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.desligar()')
            return funcoes.desligar()
                                                                                
    if True:
        resposta = chaves_funcoes.ChaveSaudacao(ListPalavras)
        if resposta >=1:
            memoria.memorizarFuncoes('funcoes.saudacao()')
            return funcoes.saudacao()
                                                                                                
    if True:
        resposta = chaves_funcoes.ChaveTradutor(ListPalavras)
        if resposta >=1:
            memoria.memorizarFuncoes('funcoes.tradutor()')
            resposta = funcoes.tradutor()
            return resposta
                    
    if True:
        resposta = chaves_funcoes.ChaveYoutube(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.siteYoutube()')
            return funcoes.siteYoutube()
        
    if True:
        resposta = chaves_funcoes.ChaveGoogle(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.Google()')
            return funcoes.Google()
                            
    if True:
        resposta = chaves_funcoes.ChaveExcel(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.Excel()')
            return funcoes.Excel()
                                
    if True:
        resposta = chaves_funcoes.ChaveNotepad(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.Notepad()')
            return funcoes.Notepad()
                                    
    if True:
        resposta = chaves_funcoes.ChaveCoinMarketCap(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.siteCoinMarketCap()')
            return funcoes.siteCoinMarketCap()
                                        
    if True:
        resposta = chaves_funcoes.ChaveAgendamento(ListPalavras)
        if resposta >= 1:
            memoria.memorizarFuncoes('funcoes.agendamento()')
            return funcoes.agendamento()
                                    
#...................................................................................................................
    else:
        pass