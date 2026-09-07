from config import ConnectionConfig

class DatabaseConnection:
    def __init__(self, config: ConnectionConfig):
        self.config = config
        self.connection = None

    def connect(self):
        """
        Simula la apertura de la conexión a la base de datos utilizando 
        las credenciales validadas.
        """
        connection_uri = (
            f"postgresql://{self.config.usuario}:***@"
            f"{self.config.host}:{self.config.puerto}/{self.config.base_de_datos}"
        )
        print(f"Conectando a la base de datos '{self.config.nombre}'...")
        print(f"URI de conexión generada: {connection_uri}")
        self.connection = True
        return True

    def is_connected(self) -> bool:
        return self.connection is not None and self.connection