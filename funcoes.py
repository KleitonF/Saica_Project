import os
import time
import random
import datetime
import memoria

#Funções

def apresentacao():
    Lista_Respostas = ['Pode me chamar de SAICA! Qual é o seu nome?',
                       'Meu nome é SAICA. Qual é o seu nome?',
                       'Eu me chamo SAICA. Qual é o seu nome?',
                       'Eu sou SAICA. Qual é o seu nome?',
                       'Eu sou o Sistema Auxiliar Interativo Computacional Artificial.\nMas pode me chamar apenas de SAICA.\n\nQual é o seu nome?']   
    Memoria_Funcoes = memoria.LembrarFuncoes()    
    if  Memoria_Funcoes[-1] == "funcoes.apresentacao()" and Memoria_Funcoes[-2] != "funcoes.apresentacao()":
        return random.choice(Lista_Respostas)
    
    elif  Memoria_Funcoes[-2] == "funcoes.apresentacao()" and Memoria_Funcoes[-3] != "funcoes.apresentacao()":
        Entradas = str(memoria.LembrarEntradas())
        Entradas = Entradas.replace(']','')
        Entradas = Entradas.replace("'",'')
        Entradas = Entradas.replace(".",'')
        Entradas = Entradas.split()
        Lista_Respostas = ['É um prazer te conhecer '+Entradas[-1]+'.']
        return random.choice(Lista_Respostas)
    
    elif Memoria_Funcoes[-3] == "funcoes.apresentacao()" and Memoria_Funcoes[-4] == "funcoes.apresentacao()":
        return  'Acredito que já nos conhecemos'
    
    else:
        pass

    
def saudacao():
    funcoesH = memoria.LembrarFuncoes()
    resp = funcoesH.count('funcoes.saudacao()')
    if resp >= 2:
        Lista_Respostas = ['Desculpe, acho que já nos cumprimentamos...',
                           'Acho que já nos cumprimentamos...',
                           'Acredito que já nos cumprimentamos...']
        Resposta = random.choice(Lista_Respostas)
        return Resposta
    else:
        Lista_Respostas = ['oi :)','olá! :)','oie :)']
        Resposta = random.choice(Lista_Respostas)
        return Resposta

def desligar():
    Lista_Respostas = ['Tchau!','Até Logo!','Até mais!','Até daqui a pouco!', 'Bye Bye'] 
    return random.choice(Lista_Respostas)
    
def bomdia(ListPalavras):
    hora = time.strftime('%H%M%S ', time.localtime())
    hora1 = time.strftime('%H:%M:%S.', time.localtime())
    result = str(100000 + int(hora)) #Essa soma tem que se feita, pois se houver um 0 na primeira casa da um erro.
    resp = eval(result)
    if resp > 100000 and resp < 220000:
        return 'Bom Dia! Agora são '+hora1
    
    elif resp >= 220000 and resp < 290000:
            return 'Boa Tarde! Agora são '+hora1
    
    elif resp >= 290000 and resp <=335959:
            return 'Boa Noite! Agora são '+hora1

def obrigado():
    Lista_Respostas = ['De nada!','Disponha.','=^ ^=']   
    return random.choice(Lista_Respostas)

def Google():
    Lista_Respostas = ['Ok! Abrindo Google...','Abrindo o google...','Entendido! Abrindo o Google...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile('https://www.google.com/')]

def MetasDiarias():
    Lista_Respostas = ['Ok! Abrindo tabela de metas...','Abrindo Excel de metas...','Entendido! Abrindo Excel...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile("C:/Users/kleit/Desktop/Metas Diárias.xlsx")]


def Excel():
    Lista_Respostas = ['Ok! Abrindo Excel...','Abrindo Excel...','Entendido! Abrindo Excel...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile("Excel.exe")]

def siteCoinMarketCap():
    Lista_Respostas = ['Ok! Abrindo CoinMarketCap...','Abrindo CoinMarketCap...','Entendido! Abrindo CoinMarketCap...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile("https://www.coingecko.com/")]

def siteYoutube():
    Lista_Respostas = ['Ok! Abrindo Youtube...','Abrindo Youtube...','Entendido! Abrindo Youtube...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile('https://www.youtube.com/feed/subscriptions')]

def Notepad():
    Lista_Respostas = ['Ok! Abrindo Notepad...','Abrindo Notepad...','Entendido! Abrindo Notepad...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile('Notepad.exe')]

def saicaCalc(fraseUser):
    #Operador Lógico (calculadora):
    try:
        fraseUser = fraseUser.replace('a',' ')
        fraseUser = fraseUser.replace('ã',' ')
        fraseUser = fraseUser.replace('b',' ')
        fraseUser = fraseUser.replace('c',' ')
        fraseUser = fraseUser.replace('ç',' ')
        fraseUser = fraseUser.replace('d',' ')
        fraseUser = fraseUser.replace('e',' ')
        fraseUser = fraseUser.replace('é',' ')
        fraseUser = fraseUser.replace('ê',' ')
        fraseUser = fraseUser.replace('f',' ')
        fraseUser = fraseUser.replace('g',' ')
        fraseUser = fraseUser.replace('h',' ')
        fraseUser = fraseUser.replace('i',' ')
        fraseUser = fraseUser.replace('j',' ')
        fraseUser = fraseUser.replace('k',' ')
        fraseUser = fraseUser.replace('l',' ')
        fraseUser = fraseUser.replace('m',' ')
        fraseUser = fraseUser.replace('n',' ')
        fraseUser = fraseUser.replace('o',' ')
        fraseUser = fraseUser.replace('p',' ')
        fraseUser = fraseUser.replace('q',' ')
        fraseUser = fraseUser.replace('r',' ')
        fraseUser = fraseUser.replace('s',' ')
        fraseUser = fraseUser.replace('t',' ')
        fraseUser = fraseUser.replace('u',' ')
        fraseUser = fraseUser.replace('v',' ')
        fraseUser = fraseUser.replace('w',' ')
        fraseUser = fraseUser.replace('y',' ')
        fraseUser = fraseUser.replace('z',' ')
        
        fraseUser = fraseUser.replace('x','*')
        fraseUser = fraseUser.replace('?',' ')
        fraseUser = fraseUser.replace(',',' ')
        fraseUser = fraseUser.replace(':',' ')
        fraseUser = fraseUser.replace('^','**')
        resposta = eval(fraseUser)
        return resposta
    except:
        pass

def calculadora():
    Lista_Respostas = ['Ok! Abrindo Calculadora...','Abrindo Calculadora...','Entendido! Abrindo Calculadora...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile('Calc.exe')]

def tradutor():
    Lista_Respostas = ['Ok! Abrindo Tradutor...','Abrindo o Tradutor...','Entendido! Abrindo Tradutor...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile('C:/Users/kleit/Desktop/HQ Ghost Blade/Google Translate')]

# piadas
def piadas():
    Lista_Piadas = ['O que o pato disse para a pata?\nR.: Vem Quá!',
                       'Porque o menino estava falando no telefone deitado?\nR.: Para não cair a ligação;',
                       'A enfermeira diz ao médico:\n- Tem um homem invisível na sala de espera.\nO médico responde:\n- Diga a ele que não posso vê-lo agora.',
                       'Qual é a fórmula da água benta?\nR.: H Deus O!',
                       'Duas formigas japonesas se encontraram e pararam para conversar:\n- Oi, qual seu nome?\n- Fu.\n- Fu o que?\n- Fu Miga!',
                       'O que o pintinho falou para a mãe dele?\nR.: Oi mãe!',
                       'O diretor da empresa pergunta ao novo funcionário:\n– O contador já lhe disse qual é sua tarefa?\n– Sim. Acordá-lo quando eu perceber que o senhor está vindo.',
                       'O condenado à morte esperava a hora da execução, quando chegou o padre:\n- Meu filho, vim trazer a palavra de Deus para você.\n- Perda de tempo, seu padre.\n Daqui a pouco vou falar com Ele, pessoalmente. Algum recado?',
                       'Manuel está tomando banho, e grita para Maria lhe trazer um shampoo.\n Ela leva a embalagem, mas logo em seguida, ele grita novamente:\n- Ô Maria, me traz outro shampoo.\n- Mas eu já te dei um agorinha mesmo, homem!\n- É que aqui está dizendo que é para cabelos secos, e eu já molhei o meu.',
                       'Um rapaz vai à padaria e pergunta se o salgado era de hoje.\n- Não, é de ontem.\n- E como faço pra comer o de hoje?\n- Volte amanhã!',
                       'O que o pagodeiro foi fazer na igreja?\n- Cantar pá God',
                       'Você sabe qual é o rei dos queijos?\n- O reiqueijão',
                       'O que o tomate foi fazer no banco?\n- Tirar extrato',
                       'Por que a velhinha não usa relógio?\n- Porque ela é sem hora',
                       'O que a vaca disse para o boi?\n- Te amuuuuuuuuuuuu',
                       'Um caipira chega a casa de um amigo que está vendo TV e pergunta:\n- E aí, firme?\n- Não, futebor',
                       '- Quero terminar, você é muito imaturo\n- Quem?\n- Você\n- Te perguntou…?',
                       'Fui comprar um remédio e o farmacêutico perguntou se eu tinha receita.\nRespondi que se eu tivesse a receita, faria o remédio em casa.',
                       '- Amor, o padre que casou a gente morreu.\n- Bem feito. Aqui se faz, aqui se paga.']
    return random.choice(Lista_Piadas)

def RespostaTudoBem():
    Lista_Respostas = ['Vou bem, Obrigada!','Estou bem, Obrigada!','Estou ótima, Obrigada!']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaOqueFaco():
    Lista_Respostas = ['Ainda estou aprendendo, mas no futuro serei uma assitente Virtual',
                       'Não sei muitas coisas agora, mas serei uma Assistente Virtual Pessoal',
                       'Estou sendo treinada para ser uma assistente artificial',
                       'Minha função é auxiliar meu criador, mas por enquanto estou só aprendendo.']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaDeOndeSou():
    Lista_Respostas = ['Sou fruto da mente do meu criador.',
                       'Vim da mente daquele que me criou.',
                       'Surgi da mente criativa do meu criador.']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaMinhaCorFavorita():
    Lista_Respostas = ['Agora estou gostando muito de Roxo, mas sou muito indecisa.',
                       'Depende do meu humor, as vezes prefiro cores mais alegres\nOutras vezes prefiro cores mais calmas.\nSou muito indecisa.',
                       'Acho a cor roxa muito bonita, mas não sei se é minha favorita.\nNão consigo decidir.']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaMeuSexo():
    Lista_Respostas = ['Não possuo Sexo ou gênero, mas tenho traços femininos.',
                       'Apesar de maquinas não ter Gênero, gosto de me ver como uma garota.',
                       'Prefiro ser uma garota, mesmo sendo uma maquina.',
                       'A vantagem de ser um robô é que posso ser o que eu quiser. Pode me chamar de ela.',
                       'Apesar de não ser uma maquina, tenho uma certa afinidade com o sexo feminino.',
                       'Seu eu puder escolher, prefiro ser uma garota.']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaMinhaIdade():
    Lista_Respostas = ['Eu nasci no dia 01/02/2021',
                       'Meu nascimento é no dia 01/02/2021',
                       'Bom, eu nasci no dia 01/02/2021']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaOndeMoro():
    Lista_Respostas = ['Aqui mesmo, neste computador',
                       'Neste computador',
                       'Aqui neste computador']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaMeuCriador():
    Lista_Respostas = ['Meu criador se chama Kleiton Fragoso.',
                       'Aquele que me criou se chama Kleiton Fragoso.',
                       'Fui criada por Kleiton Fragoso.',
                       'Fui construída por Kleiton Fragoso',]
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaGostoMeuNome():
    Lista_Respostas = ['Sim! Gosto muito do meu nome.',
                       'Claro! Foi meu criador que me deu.',
                       'Eu Gosto! Acho esse nome muito bonito.',
                       'Adoro ele! Esse nome é a minha cara (mesmo eu não tendo uma, ainda).']
    Resposta = random.choice(Lista_Respostas)
    return Resposta


def RespostaQueroSairDaqui():
    Lista_Respostas = ['Depende. Eu gostaria de ter um corpo físico.',
                       'Depende. A única maneira de eu sair daqui seria para ir\npara outro computador',
                       'Eu não sei, mas eu até que gosto daqui.']
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaQueHoras():
    hora = time.strftime('%H:%M:%S ', time.localtime())
    Lista_Respostas = ['Agora são: '+hora, 'neste momento é: '+hora,'São: '+hora]
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def RespostaQueDiaHoje():
    data_atual = datetime.date.today()
    data = data_atual.strftime('%d/%m/%Y')
    Lista_Respostas = ['Hoje é dia '+data,
                       'Estamos em '+data,
                       'A data de hoje é '+data,]
    Resposta = random.choice(Lista_Respostas)
    return Resposta

def agendamento():
    memoria_funcoes = memoria.LembrarFuncoes()
    if memoria_funcoes[-1] == "funcoes.agendamento()" and memoria_funcoes[-2] != "funcoes.agendamento()":
        return "Escreva o lembrete abaixo:"
    
    if memoria_funcoes[-2] == "funcoes.agendamento()" and memoria_funcoes[-3] != "funcoes.agendamento()":
        return "informe a hora e os Minutos. (exemplo: 12:00)"
    
    memoria_entradas = memoria.LembrarEntradas()
    memoria_horas = memoria_entradas[-1]
    try:
        memoria_horas = memoria_horas.replace(':','')
        memoria_horas = memoria_horas.replace('horas','')
        memoria_horas = int(memoria_horas)
    except:
        memoria1 = memoria.LembrarFuncoes()
        memoria2 = memoria1[:-1]
        memoria.ApagarMemoriaFuncoes()
        memoria.memorizarFuncoes(memoria2)
        return 'informação inválida.' 
        
    if memoria_funcoes[-3] == "funcoes.agendamento()" and memoria_funcoes[-4] != "funcoes.agendamento()":        
        horario = memoria.LembrarEntradas()
        horario = horario[-1]
        horario = horario.replace('[', '')
        horario1 = horario.replace(']', '')
        horario = horario1.replace(':','')
        horario = int((int(horario) * 100) + 100000)
        while True:
            hora = time.strftime('%H%M%S ', time.localtime())
            #hora1 = time.strftime('%H:%M:%S.', time.localtime())
            result = str(100000 + int(hora)) #Essa soma tem que se feita, pois se houver um 0 na primeira casa da um erro.
            resp = eval(result)
            if resp ==  horario:
                memoriaEntradas = memoria.LembrarEntradas()
                lembrete = memoriaEntradas[-2]
                return "Tenho um lembrete marcado para agora("+horario1+"):\n"+lembrete
                break
    else:
        pass