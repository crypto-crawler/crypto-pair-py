#!/usr/bin/env python3

from crypto_pair import MarketType, get_market_type, normalize_pair


def test_binance():
    assert normalize_pair('BTCUSDT', 'binance') == 'BTC/USDT'
    assert get_market_type('BTCUSD_PERP', 'binance') == MarketType.inverse_swap
