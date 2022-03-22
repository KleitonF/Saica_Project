import chaves_funcoes
import funcoes
import memoria

def SeletorFuncoes_2(ListPalavras):
    
        resposta = chaves_funcoes.ChaveBomDia(ListPalavras)
        if resposta >= 2:
            memoria.memorizarFuncoes('funcoes.bomdia(ListPalavras)')
            return funcoes.bomdia(ListPalavras)
                                                                            
        if True:
            resposta = chaves_funcoes.ChaveMetasDiarias(ListPalavras)
            if resposta >= 2:
                memoria.memorizarFuncoes('funcoes.MetasDiarias()')
                return funcoes.MetasDiarias() 
#...................................................................................................................
            else:     
                pass