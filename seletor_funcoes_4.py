import chaves_funcoes
import funcoes
import memoria

def SeletorFuncoes_4(ListPalavras):
    
    qtd = chaves_funcoes.ChavePerguntaGostoMeuNome(ListPalavras)
    if qtd >=5:
        memoria.memorizarFuncoes('funcoes.RespostaGostoMeuNome()')
        return funcoes.RespostaGostoMeuNome()
                                        
    if True:
        qtd = chaves_funcoes.ChavePerguntaDeOndeSou(ListPalavras)
        if qtd >=4:
            memoria.memorizarFuncoes('funcoes.RespostaDeOndeSou()')
            return funcoes.RespostaDeOndeSou()
                                            
    if True:
        qtd = chaves_funcoes.ChavePerguntaQueroSairDaqui(ListPalavras)
        if qtd >=4:
            memoria.memorizarFuncoes('funcoes.RespostaQueroSairDaqui()')
            return funcoes.RespostaQueroSairDaqui()
                                            
    if True:
        qtd = chaves_funcoes.ChavePerguntaMinhaCorFavorita(ListPalavras)
        if qtd >=4:
            memoria.memorizarFuncoes('funcoes.RespostaMinhaCorFavorita()')
            return funcoes.RespostaMinhaCorFavorita()
                                                    
    if True:
        resposta = chaves_funcoes.ChaveApresentacao(ListPalavras)
        if resposta >=4:
            memoria.memorizarFuncoes('funcoes.apresentacao()')
            return funcoes.apresentacao()
                    
    if True:                                
        qtd = chaves_funcoes.ChavePerguntaMeuCriador(ListPalavras)
        if qtd >= 4:
            memoria.memorizarFuncoes('funcoes.RespostaMeuCriador()')
            return funcoes.RespostaMeuCriador()
                            
    if True:
        qtd = chaves_funcoes.ChavePerguntaOqueFaco(ListPalavras)
        if qtd >= 4:
            memoria.memorizarFuncoes('funcoes.RespostaOqueFaco()')
            return funcoes.RespostaOqueFaco()
                            
    if True:
        qtd = chaves_funcoes.ChavePerguntaMeuSexo(ListPalavras)
        if qtd >= 4:
            memoria.memorizarFuncoes('funcoes.RespostaMeuSexo()')
            return funcoes.RespostaMeuSexo()
                                        
    if True:
        qtd = chaves_funcoes.ChavePerguntaMinhaIdade(ListPalavras)
        if qtd >= 4:
            memoria.memorizarFuncoes('funcoes.RespostaMinhaIdade()')
            return funcoes.RespostaMinhaIdade()
                            
    if True:
        qtd = chaves_funcoes.ChavePerguntaOndeMoro(ListPalavras)
        if qtd >= 4:
            memoria.memorizarFuncoes('funcoes.RespostaOndeMoro()')
            return funcoes.RespostaOndeMoro()
                                
    if True:
        qtd = chaves_funcoes.ChavePerguntaQueDiaHoje(ListPalavras)
        if qtd >=4:
            memoria.memorizarFuncoes('funcoes.RespostaQueDiaHoje()')
            return funcoes.RespostaQueDiaHoje()
#...................................................................................................................
    else:
        pass