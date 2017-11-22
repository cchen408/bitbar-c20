#!/usr/bin/python
# coding=utf-8
#
# <bitbar.title>C20 NAV and Asset Worth</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.desc>Displays current C20 NAV and USD asset worth</bitbar.desc>

from urllib import urlopen
url = urlopen('https://crypto20.com/status').read()

import json
result = json.loads(url)

number_of_c20 = 0  # change this to the number of C20 tokens that you own

def work():
    if result['presale'] > 0 and result['usd_value'] > 0:
        net_asset_value = float(result['nav_per_token'])
        usd_value = net_asset_value * number_of_c20
        formatted = '${:.4f} ${:,} ${:,}'.format(net_asset_value, int(usd_value), int(result['usd_value']))
        print formatted

        # print holdings
        print '---'
        holdings = result['holdings'];
        for holding in holdings:
            crypto_name = holding['name']
            crypto_value = float(holding['value'])
            crypto_percentage = crypto_value/float(result['usd_value'])*100
            print '{:s}: {:.2f}% ${:,}'.format(crypto_name, crypto_percentage, holding['value'])

work()

