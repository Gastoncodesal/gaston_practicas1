import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
from rich.console import Console
from rich.table import Table
import typer

app = typer.Typer(help="Gestor de Tareas simple en Python")
console = Console()

# Base de datos temporal en memoria
TAREAS = [
    {
        "id": 1,
        "titulo": "Diseñar estructura del proyecto",
        "vencimiento": datetime.now() + relativedelta(days=1),
        "completada": True,
    },
    {
        "id": 2,
        "titulo": "Escribir pruebas unitarias",
        "vencimiento": datetime.now() + relativedelta(days=3),
        "completada": False,
    },
]


@app.command("listar")
def listar_tareas():
    """Muestra todas las tareas registradas en una tabla formateada."""
    tabla = Table(title="Lista de Tareas")

    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("Título", style="magenta")
    tabla.add_column("Vencimiento", style="green")
    tabla.add_column("Estado", justify="center")

    for tarea in TAREAS:
        estado = "[bold green]Resuelta[/bold green]" if tarea["completada"] else "[bold red]Pendiente[/bold red]"
        fecha_str = tarea["vencimiento"].strftime("%Y-%m-%d")
        tabla.add_row(str(tarea["id"]), tarea["titulo"], fecha_str, estado)

    console.print(tabla)


@app.command("agregar")
def agregar_tarea(titulo: str):
    """Agrega una nueva tarea a la lista."""
    nueva_tarea = {
        "id": len(TAREAS) + 1,
        "titulo": titulo,
        "vencimiento": datetime.now() + relativedelta(weeks=1),
        "completada": False,
    }
    TAREAS.append(nueva_tarea)
    console.print(f"[bold blue]✓[/bold blue] Tarea '[italic]{titulo}[/italic]' agregada con éxito.")


if __name__ == "__main__":
    app()