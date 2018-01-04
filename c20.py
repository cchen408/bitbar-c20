#!/usr/bin/python

# To use this script, download and save. Using Terminal.app, change to the
# directory where you saved this file. For example, if you saved to your
# Downloads folder you will type:
#
#   cd ~/Downloads
#
# Then make this script executable by typing:
#
#   chmod +x c20.py
#
# Get BitBar from https://getbitbar.com (currently BitBar-v1.9.2.zip) and run
# it. You will be prompted for a Plugins directory. Set this to the folder where
# you saved c20.py, such as your Downloads folder and you are done.
#
# You can also set the number of c20 tokens that you own below to show how much
# your holdings are worth.

import json
from urllib import urlopen
import base64
import os.path

# change this to the number of c20 tokens that you own if you don't have a ~/.c20tokens file with the value
number_of_c20 = 0
c20tokens_path = os.path.expanduser('~') + '/.c20tokens'
if os.path.exists(c20tokens_path):
    with open(c20tokens_path, 'r') as c20tokens_file:
        number_of_c20 = float(c20tokens_file.read())

images_source = 'https://raw.githubusercontent.com/cchen408/bitbar-c20/master/token-images/{0}.png'

c20_result = json.loads(urlopen('https://crypto20.com/status').read())
top_50_result = json.loads(urlopen('https://api.coinmarketcap.com/v1/ticker/?limit=50').read())
crypto_global_result = json.loads(urlopen('https://api.coinmarketcap.com/v1/global/').read())
c20_movement_result = json.loads(urlopen('https://crypto20.com/api/v1/funds/movements').read());
token_price = {}
token_id_symbol = {}

# loop through prices rather than call api more than once
for c in top_50_result:
    symbol = str(c['symbol']).lower()
    token_price[c['id']] = float(c['price_usd'])
    token_id_symbol[c['symbol']] = c['id']

# Add custom images here
token_image_symbol = {
    'c20': 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAlCAYAAAAjt+tHAAAAAXNSR0IArs4c6QAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAACXBIWXMAABYlAAAWJQFJUiTwAAADRGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIgogICAgICAgICAgICB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyI+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDE3LTExLTIwVDA3OjExOjYzPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5QaXhlbG1hdG9yIDMuNzwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8dGlmZjpDb21wcmVzc2lvbj41PC90aWZmOkNvbXByZXNzaW9uPgogICAgICAgICA8ZXhpZjpQaXhlbFhEaW1lbnNpb24+Mjg8L2V4aWY6UGl4ZWxYRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjMyPC9leGlmOlBpeGVsWURpbWVuc2lv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',
    'market': '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'
}

# total tokens issued
tokens_issued = float(c20_result['presale'])

# NAV per token
nav_per_token = float(c20_result['nav_per_token'])

# calculate the price in eth
eth_price = float(token_price['ethereum'])
nav_eth = nav_per_token / eth_price

# calculate the price in btc
btc_price = float(token_price['bitcoin'])
nav_btc = nav_per_token / btc_price

# calculate total value
usd_value = nav_per_token * number_of_c20

# calculate total percentage you own
percentage_owned = number_of_c20 / tokens_issued

# Download and cache images from github
for token in top_50_result:
    symbol = str(token['symbol']).lower()
    if not os.path.exists('/tmp/token-images/{0}.png'.format(symbol)):
        token_url = images_source.format(symbol)
        token_image = urlopen(token_url).read()
        try:
            os.mkdir('/tmp/token-images')
        except OSError:
            pass
        with open('/tmp/token-images/{0}.png'.format(symbol), 'w') as img_file:
            img_file.write(token_image)
    else:
        with open('/tmp/token-images/{0}.png'.format(symbol), 'r') as img_file:
            token_image = img_file.read()

    token_image_symbol[symbol] = base64.b64encode(token_image)

# menu bar icon with nav
print '${:.4f}| templateImage={}'.format(nav_per_token, token_image_symbol['c20'])

# comment out line above and uncomment below if you want icon only
# menu bar icon no nav
# print '| templateImage={}'.format(token_image_symbol['c20'])

print '---'

# print nav, value of your coins, and total fund value
print 'NAV:\t${:<20.4f}\t\t12hr:  {:.4f}% | href=https://crypto20.com/en/portal/performance/ image={}'.format(nav_per_token, c20_movement_result.get('12h', 0), token_image_symbol['c20'])

# print nav in ETH and BTC with separator
print 'NAV:\t{:<20.8f}\t24hr:  {:.4f}% | href=https://crypto20.com/en/portal/performance/ image={}'.format(nav_eth, c20_movement_result.get('24h', 0), token_image_symbol['eth'])
print 'NAV:\t{:<20.8f}\t1wk:  {:.4f}% | href=https://crypto20.com/en/portal/performance/ image={}'.format(nav_btc, c20_movement_result.get('1w', 0), token_image_symbol['btc'])
print '---'

# print number of c20 you have and their value
print 'My Tokens:\t\t{:,.4f} | href=https://crypto20.com/users/ image={}'.format(number_of_c20, token_image_symbol['c20'])
print 'My Value:\t\t${:,.2f} | href=https://crypto20.com/users/ image={}'.format(usd_value, token_image_symbol['c20'])
print '---'

# tokens issues
print 'Tokens Issued:\t{:,} | href=https://crypto20.com/portal/performance/ image={}'.format(int(tokens_issued),
                                                                                             token_image_symbol['c20'])
print 'Fund Cap:\t\t${:,} | href=https://crypto20.com/portal/insights/ image={}'.format(
    int(c20_result['usd_value']), token_image_symbol['c20'])

# print total crypto market cap
print 'Market Cap:\t\t${:,} | href=https://livecoinwatch.com image={}'.format(
    int(crypto_global_result['total_market_cap_usd']), token_image_symbol['market'])

# separator bitbar recognizes and puts everything under it into a menu
print '---'

# print holdings
holdings = c20_result['holdings']

for holding in holdings:
    token_amount = float(holding['amount'])
    my_token_amount = float(token_amount * percentage_owned)
    token_symbol = holding['name']
    token_value = float(holding['value'])
    token_percentage = token_value / float(c20_result['usd_value']) * 100
    c20_value = holding['value']
    token_name = token_id_symbol[token_symbol]
    try:
        token_img = token_image_symbol[token_symbol.lower()]
    except KeyError:
        # If we don't have a symbol image, don't fail.
        token_img = ''
    crypto_price = float(token_price[token_name])

    print '{:<6s} \t{:,.2f}%\t${:<10,}\t${:<10,.2f}\t{:,.2f} | href=https://coinmarketcap.com/currencies/{:s} image={}'.format(
        token_symbol,
        token_percentage,
        c20_value,
        crypto_price,
        my_token_amount,
        token_name,
        token_img)

# Print dashboards
print "---"
print "Dashboards"
print "--youcan.dance/crypto20 | href=http://youcan.dance/crypto20"
print "--cryptodash1.firebaseapp | href=https://cryptodash1.firebaseapp.com/"
