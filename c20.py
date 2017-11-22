#!/usr/bin/python
# coding=utf-8
#
# <bitbar.title>C20 NAV and Asset Worth</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.desc>Displays current C20 NAV and USD asset worth</bitbar.desc>

from urllib import urlopen
url = urlopen('https://crypto20.com/status').read()
btg_url = urlopen('https://api.coinmarketcap.com/v1/ticker/bitcoin-gold/').read()

import json
result = json.loads(url)
btg_result = json.loads(btg_url)

number_of_c20 = 0  # change this to the number of C20 tokens that you own

symbol_path_map = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'BCH': 'bitcoin-cash',
    'XRP': 'ripple',
    'DASH': 'dash',
    'LTC': 'litecoin',
    'MIOTA': 'iota',
    'XMR': 'monero',
    'NEO': 'neo',
    'XEM': 'nem',
    'ETC': 'ethereum-classic',
    'LSK': 'lisk',
    'QTUM': 'qtum',
    'EOS': 'eos',
    'ZEC': 'zcash',
    'OMG': 'omisego',
    'ADA': 'cardano',
    'HSR': 'hshare',
    'XLM': 'stellar',
    'WAVES': 'waves',
    'PPT': 'populous',
    'STRAT': 'stratis',
    'BTS': 'bitshares',
    'ARK': 'ark'
}

def work():
    if result['presale'] > 0 and result['usd_value'] > 0:

        # calculate btg nav
        btg_val = int(float(btg_result[0]['price_usd']) * 458)
        btg_nav = float(btg_val) / float(result['presale']) * 0.98 * 0.87

        # add on top of current nav
        net_asset_value = float(result['nav_per_token']) + btg_nav
        usd_value = net_asset_value * number_of_c20

        # print nav, value of your coins, and total fund value
        print '${:.3f} ${:,} ${:,}'.format(net_asset_value, int(usd_value), btg_val + int(result['usd_value']))

        # separator bitbar recognizes and puts everything under it into a menu
        print '---'

        # print number of c20 you have
        print 'c20: {:.4f} | color=#123def href=https://crypto20.com/en/'.format(number_of_c20);

        # print holdings
        holdings = result['holdings'];
        holdings.append({'name': 'BTG', 'value': btg_val})
        for holding in holdings:
            crypto_name = holding['name']
            crypto_value = float(holding['value'])
            crypto_percentage = crypto_value/float(result['usd_value'])*100
            print '{:s}: {:.2f}% ${:,} | href=https://coinmarketcap.com/currencies/{:s}'.format(crypto_name, crypto_percentage, holding['value'], symbol_path_map[crypto_name])

work()