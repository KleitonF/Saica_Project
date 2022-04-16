import memoria

def ChaveApresentacaoMemorias():
    historico_funcoes = memoria.LembrarFuncoes()
    historico_chave = [str(historico_funcoes[-1])] + ["funcoes.apresentacao()"]
    qtd_resp = len( set( [ item for item in historico_chave if historico_chave.count( item ) > 1] ) )
    return qtd_resp

def ChaveAgendamentoMemorias():
    historico_funcoes = memoria.LembrarFuncoes()
    historico_chave = [str(historico_funcoes[-1])] + ["funcoes.agendamento()"]
    qtd_resp = len( set( [ item for item in historico_chave if historico_chave.count( item ) > 1] ) )
    return qtd_resp