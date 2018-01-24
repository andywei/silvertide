# -*- coding: UTF-8 -*-

import argparse


from bot.binance_bot import BinanceBot

if __name__ == '__main__':
    # Set parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', type=str, help='Market Symbol (Ex: XVGBTC - XVGETH)', required=True)
    parser.add_argument('--api_key', type=str, help='Binance api_key', required=True)
    parser.add_argument('--api_secret', type=str, help='Binance api_secret', required=True)

    options = parser.parse_args()

    # Get start
    bot = BinanceBot(options)
    bot.run()
