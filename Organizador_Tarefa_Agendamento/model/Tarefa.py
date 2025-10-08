from datetime import datetime

class Tarefa:
    def __init__(self, nome_tarefa, descricao=None, data_realizacao=None):
        self.__nome = nome_tarefa
        self.__concluido = False
        self.__descricao = descricao
        self.__data_realizacao = data_realizacao

    def concluir(self):
        self.__concluido = True

    def exibir_dados(self):
        status = "CONCLUIDO" if self.__concluido == True else "A FAZER"
        return f"Tarefa cadastrada: {self.__nome} [Concluída? {status}]"
    
    def __eq__(self, outro):
        if(self.nome == outro.nome and self.data_realizacao == outro.data_realizacao):
            return True
        else:
            return False
        
    def __str__(self):
        # Inclui descrição se existir
        desc = f" - {self.descricao}" if self.descricao else ""
        status = "CONCLUIDO" if getattr(self, "_Tarefa__concluido") else "A FAZER"
        return f"{self.nome}{desc} [Concluída? {status}]"

#------------------------------------------------#

    @property
    def nome(self):
        return (self.__nome).upper()
    
    @nome.setter
    def nome(self, nome_tarefa):
        self.__nome = nome_tarefa.title()

#------------------------------------------------#

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, desc):
        self.__descricao = desc

#------------------------------------------------#

    @property
    def data_realizacao(self):
        return self.__data_realizacao

    @data_realizacao.setter
    def data_realizacao(self, data):
        try:
            self.__data_realizacao = datetime.strptime(data, "%d-%m-%Y")
        except ValueError as e:
            if data != None:
                self.__data_realizacao = None
            else:
                print(f"Data em formato inválido: {e}")

#------------------------------------------------#
