# Importando Bibliotecas
from app import create_app
from app.core.env_loader import Env


# Inicializa ao executar o arquivo
if __name__ == "__main__":

    # Instanciando Aplicação
    app = create_app()
    
    # Rodando Aplicação
    app.run(
        port=Env.require("APP_PORT"),  # Porta
        host=Env.require("APP_HOST"),  # Host
        debug=Env.require("APP_DEBUG") # Modo Debug
    )