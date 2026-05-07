from models.TareasModel import TareaModel


class TareaController:

    def __init__(self):
        self.model = TareaModel()

    def obtener_lista(self, idUs):

        return self.model.listar_por_usuario(idUs)

    def guardar_nueva(self, idUs, titulo, descripcion, prioridad, clasificacion):

        if not titulo:
            return False, "El titulo es obligatorio"

        self.model.crear(
            idUs,
            titulo,
            descripcion,
            prioridad,
            clasificacion
        )

        return True, "Tarea guardada"
