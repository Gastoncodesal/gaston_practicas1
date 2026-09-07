import os
from dotenv import load_dotenv

# Carga las variables de entorno definidas en el archivo .env
load_dotenv()

class ConnectionConfig:
    def __init__(self):
        # Mapeo de atributos y las variables de entorno correspondientes
        self.nombre = self._get_required_env("DB_NAME")
        self.host = self._get_required_env("DB_HOST")
        self.puerto = self._parse_port(self._get_required_env("DB_PORT"))
        self.usuario = self._get_required_env("DB_USER")
        self.contrasena = self._get_required_env("DB_PASSWORD")
        self.base_de_datos = self._get_required_env("DB_DATABASE")

    def _get_required_env(self, key: str) -> str:
        """Obtiene una variable de entorno y valida que no esté vacía."""
        value = os.getenv(key)
        if value is None or value.strip() == "":
            raise ValueError(f"Error de Configuración: La variable de entorno '{key}' es obligatoria y no está configurada.")
        return value.strip()

    def _parse_port(self, port_str: str) -> int:
        """Convierte el puerto de texto a entero."""
        try:
            return int(port_str)
        except ValueError:
            raise ValueError(f"Error de Configuración: El puerto '{port_str}' no es un número entero válido.")

    def __str__(self):
        """Representación segura en formato texto (ocultando la contraseña)."""
        return (
            f"Configuración [{self.nombre}]:\n"
            f"  Host: {self.host}\n"
            f"  Puerto: {self.puerto}\n"
            f"  Usuario: {self.usuario}\n"
            f"  Base de datos: {self.base_de_datos}"
        )