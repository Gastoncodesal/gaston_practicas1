from datetime import datetime
from src.main import TAREAS, agregar_tarea


def test_inicializacion_tareas():
    """Verifica que la lista inicial de tareas contenga elementos."""
    assert len(TAREAS) == 2
    assert TAREAS[0]["completada"] is True


def test_agregar_tarea():
    """Verifica que se agreguen tareas correctamente a la lista."""
    cantidad_inicial = len(TAREAS)
    nuevo_titulo = "Estudiar para el examen"

    agregar_tarea(nuevo_titulo)

    assert len(TAREAS) == cantidad_inicial + 1
    assert TAREAS[-1]["titulo"] == nuevo_titulo
    assert TAREAS[-1]["completada"] is False
    assert isinstance(TAREAS[-1]["vencimiento"], datetime)