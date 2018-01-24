from binance.client import Client
from binance.websockets import BinanceSocketManager


class BinanceBot(object):

    def __init__(self, options):
        self.options = options
        self.client = Client(options.api_key, options.api_secret)
        self.socket_manager = BinanceSocketManager(self.client)
        self.socket_manager.start_aggtrade_socket(options.symbol, self.process_message)

    def run(self):
        self.socket_manager.start()

    @staticmethod
    def process_message(msg):
        print("message type: {}".format(msg['e']))
        print(msg)
