import chaves_funcoes_memorias
import funcoes
import memoria


def SeletorFuncoesMemorias():
    
    resposta = chaves_funcoes_memorias.ChaveApresentacaoMemorias()
    if resposta >=1:
        memoria.memorizarFuncoes("funcoes.apresentacao()")
        return funcoes.apresentacao()
    
    elif True:
        resposta = chaves_funcoes_memorias.ChaveAgendamentoMemorias()
        if resposta >= 1:
            memoria.memorizarFuncoes("funcoes.agendamento()")
            return funcoes.agendamento()
    
        else:
            pass