Crypto20 Bitbar Plugin
---

Download BitBar https://getbitbar.com/

1. Copy `c20.py` into your bitbar plugins directory
2. In the command prompt run ```chmod 755 c20.py```
3. Create a ~/.c20tokens file with the number of tokens you own
4. Refresh your bitbar

Description
--- 
#### c20.py
* nav in ETH and BTC
* market cap links to https://livecoinwatch.com/
* individual holdings link to their respective page on coinmarketcap
* added dashboard links to youcandance & firebaseapp
* added the amount of each holding you technically hold with your tokens
* added nav movements
* added staked earnings 1/17/2018

### generate_images.py
1. The `c20.py` script grabs token images from the github repo
2. The devs are responsible for generating them as new coins enter the market. This is done by running `python bin/generate_images.py`. You'll need to install the `pillow` dep and push the resultant generated images back to the repo for the clients to consume.
3. The `c20.py` script caches token images locally so github isn't hit often.

### Python Error Fixes

***Error:***
```
IOError: [Errno socket error] [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590)
``` 

***Solution:***
```
brew upgrade openssl
brew rm python
brew install python --with-brewed-openssl
```

change line 1 in c20.py to
```
#!/usr/local/bin/python2
```

---

Screenshots
---
![chris](https://raw.githubusercontent.com/cchen408/bitbar-c20/master/screenshots/chris.png)

Contributors
---
* [chrischen](https://github.com/cchen408)
* [kiva](https://github.com/michaelwookey)
* [hobbsAU](https://github.com/hobbsAU)
* [themadcanudist](https://github.com/themadcanudist)
