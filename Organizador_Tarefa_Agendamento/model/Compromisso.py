from model.Tarefa import Tarefa
from model.Agendamento import Agendamento

class Compromisso(Tarefa, Agendamento):
    def __init__(self, nome, descricao=None, titulo=None, data_inicio=None, data_final=None, local=None):
        # Inicializa Tarefa (sem data_realizacao)
        Tarefa.__init__(self, nome, descricao)
        # Inicializa Agendamento
        Agendamento.__init__(self, titulo, data_inicio, data_final, local)

    def __str__(self):
        return (f"[Compromisso] {self.nome} ({self.descricao}) | "
                f"Título: {self.titulo} | {self.data_inicio} - {self.data_final} "
                f"| Local: {self.local}")
