# Importando bibliotecas
from flask import Flask
from app.core.env_loader import EnvLoader

# Função para criar aplicação
def create_app():

    # Instanciando aplicação
    app = Flask(__name__)

    # Retornando aplicação
    return app