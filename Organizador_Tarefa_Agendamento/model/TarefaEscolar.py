from model.Tarefa import Tarefa

class TarefaEscolar(Tarefa):
    def __init__(self, nome_tarefa, disciplina, descricao=None, data_realizacao=None, peso=0, data_entrega=None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        
        self.__disciplina = disciplina
        self.__peso = peso
        self.data_entrega = data_entrega
        
    # Getter e Setter para disciplina
    def get_disciplina(self):
        return self.__disciplina

    def set_disciplina(self, nova_disciplina):
        self.__disciplina = nova_disciplina

    # Getter e Setter para peso
    def get_peso(self):
        return self.__peso

    def set_peso(self, novo_peso):
        if novo_peso >= 0:
            self.__peso = novo_peso
        else:
            raise ValueError("O peso não pode ser negativo.")

    # Getter e Setter para data_entrega
    def get_data_entrega(self):
        return self.data_entrega

    def set_data_entrega(self, nova_data):
        self.data_entrega = nova_data

    def __str__(self):
        return f"[Tarefa Escolar] {super().__str__()} | Disciplina: {self.__disciplina} | Peso: {self.__peso} | Data de entrega: {self.data_entrega}"


        