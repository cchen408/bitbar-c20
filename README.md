Crypto20 Bitbar Plugin
---

Download BitBar https://getbitbar.com/

1. Copy `c20.py` into your bitbar plugins directory
2. In the command prompt run ```chmod 755 c20.py```
3. Refresh your bitbar

Description
--- 
#### c20.py
* nav in ETH and BTC
* market cap links to https://livecoinwatch.com/
* individual holdings link to their respective page on coinmarketcap
* added dashboard links to youcandance & firebaseapp
* added the amount of each holding you technically hold with your tokens
* added nav movements

#### c20-icon.py
* compact version at top with only the icon in your menu bar

#### c20-full.py
* includes a lot more info
* dev can add more here

Token Images
---
1. The `c20.py` script grabs token images from the github repo
2. The devs are responsible for generating them as new coins enter the market. This is done by running `generate_images.py`. You'll need to install the `pillow` dep and push the resultant generated images back to the repo for the clients to consume.
3. The `c20.py` script caches token images locally so github isn't hit often.

## Screenshots
---
![chris](https://raw.githubusercontent.com/cchen408/bitbar-c20/master/screenshots/chris.png)

Contributors
---
* ([chrischen](https://github.com/cchen408))
* ([kiva](https://github.com/michaelwookey))
* ([hobbsAU](https://github.com/hobbsAU)) - c20-full.py
* ([themadcanudist](https://github.com/themadcanudist))
