import sys
import yaml
import socket
import logging

import config
from rss.recognize import get_text_from_speach


ADDR = config.STT_SOCKET_HOST, config.STT_SOCKET_PORT
CHANNEL_SIZE = config.STT_SOCKET_CH_SIZE


def __load_logging():
    if config.IS_DEVELOP:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    else:
        with open(config.LOGGING_CONFIG_PATH, 'r') as f:
            config_d = yaml.safe_load(f.read())
            logging.config.dictConfig(config_d)


def main():
    __load_logging()
    logger = logging.getLogger('rss')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    logger.info(f'Socket is listening on {ADDR}')
    while True:
        conn, addr = server.accept()
        logger.info(f'Got connection {addr}.')
        data = b''
        recv_data = conn.recv(CHANNEL_SIZE)
        logger.info(f'Getting data {addr}.')
        while recv_data:
            data += recv_data
            recv_data = conn.recv(CHANNEL_SIZE)
        logger.info(f'Data received {addr}.')
        text = get_text_from_speach(data)
        logger.info(f'Recognition done {addr}.')
        conn.send(f'{text}\n'.encode())
        logger.info(f'Response is sent {addr}.')
        conn.close()
        logger.info(f'Connection is closed {addr}.')


if __name__ == "__main__":
    main()
    # Check from terminal
    # cat ./assets/love-story.mp3 | nc localhost 4456 -q0
