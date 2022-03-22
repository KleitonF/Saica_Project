# Dialogos: Perguntas e Respostas

def ChaveAgendamento(ListPalavras):
    chave = ['agendamento']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaTudoBem(ListPalavras):
    chave = ['tudo','bem','como','vai','está','você','vc','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaDeOndeSou(ListPalavras):
    chave = ['de','onde','vem','vc','você','é','veio','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaMeuCriador(ListPalavras):
    chave = ['construida','construída','quem','seu','criador','te','construiu','fez','sistema','criador','criou','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaQueroSairDaqui(ListPalavras):
    chave = ['pretende','desejo','deseja','tem','vontade','gostaria','sair','desse','?','deste','pc','computador','sistema','quer','daí']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaOqueFaco(ListPalavras):
    chave = ['fazer','sabe','que','você','vc','faz','vida','qual','seu','trabalho','sua','função','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaGostoMeuNome(ListPalavras):
    chave = ['você','vc','gosta','seu','nome','saica','acha','bonito','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaMinhaCorFavorita(ListPalavras):
    chave = ['qual','cor','favorita','mais','gosta','preferida','você','vc','sua','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaMeuSexo(ListPalavras):
    chave = ['qual','seu','sexo','genero','você','vc','homem','mulher','menino','menina','macho','femea',
             'masculino','feminino','feminina','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaMeuNome(ListPalavras):
    chave = ['quem','fala','nome','qual','seu','chama','como','você','vc','tem','diga','diz','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveApresentacao(ListPalavras):
    #Palavras-Chave dos inputs do user
    chaveEntradas = ['quem','fala','nome','qual','seu','chama','como','você','vc','tem','diga','diz','?']
    fraseUser_chave = ListPalavras + chaveEntradas
    qtd_user = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd_user

def ChavePerguntaMinhaIdade(ListPalavras):
    chave = ['quantos','anos','você','vc','tem','idade','sua','qual','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaOndeMoro (ListPalavras):
    chave = ['onde','você','vc','mora','está','tá','nasceu','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaQueDiaHoje(ListPalavras):
    chave = ['que','dia','hoje','em','data','estamos','qual','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePerguntaQueHoras(ListPalavras):
    chave = ['que','horas','agora','são','em','horario','qual','?']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd
#---------------------------------------------------------------------------------------------------
# Chaves_Comandos

def ChaveGoogle(ListPalavras):
    chave = ['google','navegador']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveYoutube(ListPalavras):
    chave = ['youtube']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveExcel(ListPalavras):
    chave = ['excel']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveMetasDiarias(ListPalavras):
    chave = ['metas','diárias','diarias']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveTradutor(ListPalavras):
    chave = ['tradutor']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveCoinMarketCap(ListPalavras):
    chave = ['marketcap','coinmarketcap']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveNotepad(ListPalavras):
    chave = ['notepad','notas','anotação','nota','note']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveSaudacao(ListPalavras):
    chave = ['oi','olá','oie','eai','ola']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveDesligar(ListPalavras):
    chave = ['desligar','tchau','desliga','xau','fim','adeus']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveObrigado(ListPalavras):
    chave = ['obrigado','obrigada','obg','vlw','agradeço']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveBomDia(ListPalavras):
    chave = ['bom','dia','boa','tarde','noite']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChaveCalculadora(ListPalavras):
    chave = ['calculadora','calcular','calcule','calculo']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd

def ChavePiadas(ListPalavras):
    chave = ['conte','uma','1','piada','conta','me','outra']
    fraseUser_chave = ListPalavras+chave
    qtd = len( set( [ item for item in fraseUser_chave if fraseUser_chave.count( item ) > 1] ) )
    return qtd