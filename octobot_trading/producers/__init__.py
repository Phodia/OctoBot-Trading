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

from octobot_trading.producers.prices_updater import MarkPriceUpdater
from octobot_trading.producers.kline_updater import KlineUpdater
from octobot_trading.producers.ticker_updater import TickerUpdater
from octobot_trading.producers.recent_trade_updater import RecentTradeUpdater
from octobot_trading.producers.order_book_updater import OrderBookUpdater
from octobot_trading.producers.ohlcv_updater import OHLCVUpdater
from octobot_trading.producers.funding_updater import FundingUpdater
from octobot_trading.producers.trades_updater import TradesUpdater
from octobot_trading.producers.positions_updater import PositionsUpdater
from octobot_trading.producers.orders_updater import OrdersUpdater
from octobot_trading.producers.balance_updater import BalanceProfitabilityUpdater, BalanceUpdater


class MissingOrderException(Exception):

    def __init__(self, order_id):
        self.order_id = order_id


def get_unauthenticated_updater_producers():
    return [OHLCVUpdater, OrderBookUpdater, RecentTradeUpdater, TickerUpdater,
            KlineUpdater, MarkPriceUpdater, FundingUpdater]


def get_authenticated_updater_producers():
    return [BalanceUpdater, OrdersUpdater, TradesUpdater,
            PositionsUpdater, BalanceProfitabilityUpdater]
