from model.Tarefa import Tarefa

class TarefaProfissional(Tarefa):
    def __init__(self, nome, descricao, projeto, data_entrega):
        super().__init__(nome, descricao)
        self.projeto = projeto
        self.data_entrega = data_entrega

    def __str__(self):
        return (f"[Profissional] {super().__str__()} | Projeto: {self.projeto} | "
                f"Entrega: {self.data_entrega}")
