import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN: str = os.getenv('API_TOKEN', '')

STT_SOCKET_HOST: str = os.getenv('STT_SOCKET_HOST', 'localhost')
STT_SOCKET_PORT: int = int(os.getenv('STT_SOCKET_PORT', 4456))
STT_SOCKET_CH_SIZE: int = int(os.getenv('STT_SOCKET_CH_SIZE', 1024))
LOGGING_CONFIG_PATH: str = 'logging.yaml'

IS_DEVELOP: str = bool(os.getenv('IS_DEVELOP', False))
