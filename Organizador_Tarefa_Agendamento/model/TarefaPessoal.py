from model.Tarefa import Tarefa

class TarefaPessoal(Tarefa):
    def __init__(self, nome, descricao, tipo):
        super().__init__(nome, descricao)
        self.tipo = tipo  # saúde, lazer, doméstica, etc.

    def __str__(self):
        return f"[Pessoal] {super().__str__()} | Tipo: {self.tipo}"
