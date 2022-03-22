import memoria

def ChaveApresentacaoMemorias():
     chave_respostas = ['Pode me chamar de SAICA!\nQual é o seu nome?','Meu nome é SAICA.\nQual é o seu nome?','Eu me chamo SAICA.\nQual é o seu nome?',
                       'Eu sou SAICA.\nQual é o seu nome?','Eu sou o Sistema Auxiliar Interativo Computacional Artificial.\nMas pode me chamar apenas de SAICA.\nQual é o seu nome?']
     historico_respostas = memoria.LembrarRespostas()
     historico_chave = [str(historico_respostas[-1])] + chave_respostas
     qtd_resp = len( set( [ item for item in historico_chave if historico_chave.count( item ) > 1] ) )
     return qtd_resp

def ChaveAgendamentoMemorias():
    historico_funcoes = memoria.LembrarFuncoes()
    historico_chave = [str(historico_funcoes[-1])]+["funcoes.agendamento()"]
    qtd_resp = len( set( [ item for item in historico_chave if historico_chave.count( item ) > 1] ) )
    return qtd_resp