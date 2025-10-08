from datetime import date

from model.Tarefa import Tarefa
from model.TarefaPessoal import TarefaPessoal
from model.Compromisso import Compromisso
from model.Agendamento import Agendamento
from model.TarefaProfissional import TarefaProfissional





if __name__ == "__main__":
    # Criando tarefas
    t1 = TarefaProfissional("Reunião", "Planejamento do projeto", "Projeto X", date(2025, 10, 7))
    t2 = TarefaPessoal("Academia", "Treino de perna", "Saúde")

    # Criando agendamento
    ag = Agendamento("Planejamento Semanal", date(2025, 10, 5), date(2025, 10, 7), "Sala 101")
    ag.adicionar_atividade(t1)
    ag.adicionar_atividade(t2)

    # Criando compromisso
    c1 = Compromisso("Entrevista", "Vaga estágio", "Entrevista Empresa Y", 
                     date(2025, 10, 6), date(2025, 10, 6), "Online")

print(t1, end="\n\n")  
print(t2, end="\n\n")
print(ag, end="\n\n")
print(c1, end="\n\n")
