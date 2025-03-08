from SRC.model.errores_actividad import ErrorFechaHoraInvalida
from SRC.model.supervisor import Supervisor
from _datetime import datetime

class Archivo:
    def __init__(self, nombre: str, tipo: str, ruta: str):
        self.Ruta = ruta
        self.Tipo = tipo
        self.Nombre = nombre

    def subir_archivo(self):
        pass

class Actividad:
    
    def __init__(self, idactividad: int, fechahora: str, responsable: str, descripcion: str, condicionesclimaticas: str, anexos: list[Archivo], supervisor: Supervisor):

        try:
            self.FechaHora = datetime.strptime(fechahora, "%Y-%m-%d %H:%M:%S")
        except ValueError:
                # Si falla, lanzamos la excepción personalizada
            raise ErrorFechaHoraInvalida("Formato incorrecto de fecha y hora")
        self.Supervisor = supervisor
        self.Anexos = anexos
        self.CondicionesClimaticas = condicionesclimaticas
        self.Descripcion = descripcion
        self.Responsable = responsable
        self.idActividad = idactividad
        

    def registrar_actividad(self):
        pass
    
    def consultar_actividad(self):
        pass
    
    def eliminar_archivo(self):
        pass