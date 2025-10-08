class Agendamento:
    def __init__(self, titulo, data_inicio, data_final, local, atividades=[]):
        self.titulo = titulo
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.local = local
        self.atividades = atividades  # lista de objetos Tarefa

    def adicionar_atividade(self, atividade):
        self.atividades.append(atividade)

    def __str__(self):
        atividades_txt = ", ".join([a.nome for a in self.atividades])
        return (f"Agendamento: {self.titulo} | {self.data_inicio} - {self.data_final} "
                f"| Local: {self.local} | Atividades: {atividades_txt}")
