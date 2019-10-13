#  Drakkar-Software OctoBot-Trading
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.

from octobot_commons.logging.logging_util import get_logger

from octobot_trading.exchanges.data.exchange_symbol_data import ExchangeSymbolData


class ExchangeSymbolsData:
    def __init__(self, exchange_manager):
        self.logger = get_logger(self.__class__.__name__)
        self.exchange_manager = exchange_manager
        self.exchange = exchange_manager.exchange
        self.config = exchange_manager.config
        self.exchange_symbol_data = {}

    def get_exchange_symbol_data(self, symbol):
        try:
            return self.exchange_symbol_data[symbol]
        except KeyError:
            self.exchange_symbol_data[symbol] = ExchangeSymbolData(self.exchange_manager, symbol)
            return self.exchange_symbol_data[symbol]
