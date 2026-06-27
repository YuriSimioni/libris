# Importando bibliotecas
import os
from pathlib import Path
from dotenv import load_dotenv

# Localizando diretório root da aplicação
ROOT_DIR = Path(__file__).resolve().parents[2]

# Carregando variaveis do .env
load_dotenv(ROOT_DIR / ".env", override=True)


# Classe para variaveis
class Env:
    @staticmethod
    def get(key: str, default=None):
        return os.getenv(key, default)

    @staticmethod
    def require(key: str):
        value = os.getenv(key)
        if value is None:
            raise RuntimeError(f"Variável '{key}' não encontrada.")
        return value