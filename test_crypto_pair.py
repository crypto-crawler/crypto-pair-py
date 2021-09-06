#!/usr/bin/env python3

from crypto_pair import normalize_pair


def test_binance():
    assert normalize_pair('BTCUSDT', 'binance') == 'BTC/USDT'
