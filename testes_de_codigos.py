import os
import time
import random
from classe_saica import Saica
#--------------------------------------------------------------------------------------

#Teste de agendamento de atividade (Funcionando!)
def agendamento():
    Saica.Resposta(Saica, 'Informe a Hora e os Minutos')
    FraseUser, ListPalavras = Saica.Entrada(Saica)
    Saica.Resposta(Saica, 'Agendado!')
    horario = FraseUser.replace(':','')
    
    horario = int((int(horario) * 100) + 100000)
    while True:   
        hora = time.strftime('%H%M%S ', time.localtime())
        #hora1 = time.strftime('%H:%M:%S.', time.localtime())
        result = str(100000 + int(hora)) #Essa soma tem que se feita, pois se houver um 0 na primeira casa da um erro.
        resp = eval(result)
        if resp ==  horario:
            MetasDiarias()
            break

def MetasDiarias():
    Lista_Respostas = ['Ok! Abrindo tabela de metas...','Abrindo Excel de metas...','Entendido! Abrindo Excel...']
    Resposta = random.choice(Lista_Respostas)
    return [Resposta, os.startfile("C:/Users/kleit/Desktop/Metas Diárias.xlsx")]
#--------------------------------------------------------------------------------------

