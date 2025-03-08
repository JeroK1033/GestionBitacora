import datetime
import pytest

from SRC.model.errores_actividad import ErrorDescripcion,ErrorFechaHora,ErrorFechaHoraInvalida
from SRC.model.actividad import Actividad,Archivo
from SRC.model.supervisor import Supervisor

# Primera Funcionalidad

# Casos de Error

def test_registrar_actividad_fechahora_invalida():
    with pytest.raises(ErrorFechaHoraInvalida, match="Formato incorrecto de fecha y hora"):
        supervisor = Supervisor("Juan", "juan@gmail.com", "juan123")
        anexos = ["anexo1", "anexo2"]
        actividad = Actividad(9, "FECHA INVALIDA", "Juan", "Cimientos Listos", "Soleado", anexos, supervisor)
        actividad.registrar_actividad()


def test_registrar_con_fecha_hora_vacia():
    supervisor = Supervisor("Pedro", "pedro@gmail.com", "pedro123")
    anexos = []
    actividad = Actividad(8, None, "Pedro", "Muros Parados", "Lluvioso", anexos, supervisor, )
    with pytest.raises(ErrorFechaHora):
        actividad.registrar_actividad()


def test_registrar_actividad_sin_descripcion():
    with pytest.raises(ErrorDescripcion, match="La descripcion esta vacia"):
        supervisor = Supervisor("Daniel", "daniel@gmail.com", "daniel124")
        anexos = []
        actividad = Actividad(7, datetime(2025, 10, 4, 10, 45), "Daniel", None, "Nublado", anexos, supervisor)
        actividad.registrar_actividad


# Casos Extremos

def test_registrar_actividad_con_maximo_anexos():
    supervisor = Supervisor("Ana Torres", "ana@example.com", "contraseña101")
    anexos = [Archivo(f"archivo{i}.txt", "txt", f"/ruta/archivo{i}.txt") for i in range(100)]
    actividad = Actividad(4, datetime(2023, 10, 3, 11, 0), "Ana Torres", "Revisión de informes", "Lluvia", anexos,
                          supervisor)
    assert actividad.registrar_actividad() == "Actividad registrada con éxito"


def test_registrar_actividad_en_limite_de_tiempo():
    supervisor = Supervisor("Luis Gomez", "luis@example.com", "contraseña202")
    actividad = Actividad(5,(2023, 10, 3, 23, 59), "Luis Gomez", "Cierre de proyecto", "Despejado", [],
                          supervisor)
    assert actividad.registrar_actividad() == "Actividad registrada con éxito"


def test_registrar_actividad_con_fecha_hora_en_mismo_momento():
    supervisor = Supervisor("Elena Martinez", "elena@example.com", "contraseña303")
    actividad = Actividad(6, datetime.now(), "Elena Martinez", "Inicio de nuevo proyecto", "Soleado", [], supervisor)
    assert actividad.registrar_actividad() == "Actividad registrada con éxito"


# Casos de Prueba Normal

def test_registrar_actividad_normal():
    supervisor = Supervisor("Lucas", "lucas@gmail.com", "Lucas-123")
    anexos = [Archivo("documento1.pdf", "pdf", "/ruta/documento1.pdf")]
    actividad = Actividad(1, datetime(2023, 10, 1, 10, 30), "Lucas", "Revisión de proyecto", "Soleado", anexos,
                          supervisor)
    assert actividad.registrar_actividad() == "Actividad registrada con éxito"


def test_registrar_actividad_con_anexos():
    supervisor = Supervisor("Maria", "maria@gmail.com", "MariaA4-33")
    anexos = [Archivo("imagen1.png", "png", "/ruta/imagen1.png"),
              Archivo("documento2.docx", "docx", "/ruta/documento2.docx")]
    actividad = Actividad(2, datetime(2023, 10, 2, 14, 0), "Maria", "Reunión de equipo", "Nublado", anexos, supervisor)
    assert actividad.registrar_actividad() == "Actividad registrada con éxito"


def test_registrar_actividad_en_dia_futuro():
    supervisor = Supervisor("Carlos ", "carlos@gmail.com", "carlitos79/88")
    anexos = []
    actividad = Actividad(3, datetime(2023, 12, 1, 9, 0), "Carlos Ruiz", "Planificación de proyecto", "Despejado",
                          anexos, supervisor)
    assert actividad.registrar_actividad() == "Actividad registrada con éxito"


# Funcionalidad 2


def actividades_prueba(module):
    # Crear un supervisor y registrar algunas actividades
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    actividades = [
        Actividad(1, datetime(2023, 10, 1, 10, 30), "Juan Perez", "Revisión de proyecto", "Soleado", [], supervisor),
        Actividad(2, datetime(2023, 10, 2, 14, 0), "Juan Perez", "Reunión de equipo", "Nublado", [], supervisor),
        Actividad(3, datetime(2023, 10, 3, 9, 0), "Juan Perez", "Planificación de proyecto", "Despejado", [],
                  supervisor),
    ]
    for actividad in actividades:
        actividad.registrar_actividad()


# Casos Normales
def test_consultar_actividades_en_rango():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 10, 1)
    fin = datetime(2023, 10, 3)

    actividades = supervisor.consultar_actividades(inicio, fin)

    assert len(actividades) == 3  # Debería devolver 3 actividades


def test_consultar_actividades_en_rango_con_un_dia():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 10, 2)
    fin = datetime(2023, 10, 2)

    actividades = supervisor.consultar_actividades(inicio, fin)

    assert len(actividades) == 1  # Debería devolver 1 actividad


def test_consultar_actividades_en_rango_vacio():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 10, 4)
    fin = datetime(2023, 10, 5)

    actividades = supervisor.consultar_actividades(inicio, fin)

    assert len(actividades) == 0  # No debería devolver actividades


# Casos Extremos
def test_consultar_actividades_en_rango_extremo():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 10, 1)
    fin = datetime(2023, 10, 10)  # Rango más amplio

    actividades = supervisor.consultar_actividades(inicio, fin)

    assert len(actividades) == 3  # Debería devolver 3 actividades


def test_consultar_actividades_con_rango_mismo_dia():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 10, 1, 0, 0)
    fin = datetime(2023, 10, 1, 23, 59)

    actividades = supervisor.consultar_actividades(inicio, fin)

    assert len(actividades) == 1  # Debería devolver 1 actividad


def test_consultar_actividades_con_rango_inverso():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 10, 3)
    fin = datetime(2023, 10, 1)

    actividades = supervisor.consultar_actividades(inicio, fin)

    assert len(actividades) == 0


# Casos Error
def test_consultar_actividades_con_fechas_invalidas():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = None
    fin = datetime(2023, 10, 3)

    with pytest.raises(ErrorRangoFechas):
        supervisor.consultar_actividades(inicio, fin)


def test_consultar_actividades_con_fechas_invalidad():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 10, 4)
    fin = "fecha_invalida"

    with pytest.raises(ErrorRangoFechas):
        supervisor.consultar_actividades(inicio, fin)


def test_consultar_actividades_con_fechas_futuras():
    supervisor = Supervisor("Juan Perez", "juan@example.com", "contraseña123")
    inicio = datetime(2023, 12, 1)
    fin = datetime(2023, 12, 31)
    actividades = supervisor.consultar_actividades(inicio, fin)
    assert len(actividades) == 0
