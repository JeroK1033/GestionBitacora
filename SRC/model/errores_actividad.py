class ErrorDescripcion(Exception):
    def __init__(self,):
        super().__init__(f"La descripción no puede estar vacía")
        
class ErrorFechaHora(Exception):
    def __init__(self,):
        super().__init__(f"La fecha y hora no pueden estar vacías")
    
class ErrorFechaHoraInvalida(Exception):
    def __init__(self,):
        super().__init__(f"Formato incorrecto de fecha y hora")
