import sys
from config import ConnectionConfig
from conections import DatabaseConnection

def main():
    print("--- Cargando configuración desde el entorno ---")
    try:
        # Cargar y validar variables de entorno
        config = ConnectionConfig()
        print("Variables de entorno cargadas con éxito:\n")
        print(config)
        print("-" * 45)

        # Probar el inicio de la conexión
        db_conn = DatabaseConnection(config)
        db_conn.connect()

        if db_conn.is_connected():
            print("\n¡Prueba exitosa! La conexión fue establecida correctamente con los datos de .env.")

    except ValueError as err:
        print(f"\n[ERROR DE VALIDACIÓN] {err}", file=sys.stderr)
        sys.exit(1)
    except Exception as err:
        print(f"\n[ERROR INESPERADO] {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()