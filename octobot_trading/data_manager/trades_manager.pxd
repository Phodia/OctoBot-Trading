# cython: language_level=3
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
#  Lesser General License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
from octobot_trading.data.trade cimport Trade
from octobot_trading.util.initializable cimport Initializable


cdef class TradesManager(Initializable):
    cdef object logger

    cdef public object trades

    cdef void _check_trades_size(self)
    cdef void _reset_trades(self)
    cdef Trade _create_trade_from_raw(self, dict raw_trade)
    cdef void _remove_oldest_trades(self, int nb_to_remove)

    cpdef bint upsert_trade(self, str trade_id, dict raw_trade)