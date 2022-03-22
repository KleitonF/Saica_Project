import chaves_funcoes
import funcoes
import memoria

def SeletorFuncoes_3(ListPalavras):
    
    qtd = chaves_funcoes.ChavePerguntaQueHoras(ListPalavras)
    if qtd >=3:
        memoria.memorizarFuncoes('funcoes.RespostaQueHoras()')
        return funcoes.RespostaQueHoras()
                   
    if True:
        qtd = chaves_funcoes.ChavePerguntaTudoBem(ListPalavras)
        if qtd >= 3:
            memoria.memorizarFuncoes('funcoes.RespostaTudoBem()')
            return funcoes.RespostaTudoBem()    
        
    if True:
        resposta = chaves_funcoes.ChavePiadas(ListPalavras)
        if resposta >= 3:
            memoria.memorizarFuncoes('funcoes.piadas()')
            return funcoes.piadas()
#...................................................................................................................
    else:
        pass